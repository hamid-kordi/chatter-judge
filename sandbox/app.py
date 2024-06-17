import os
import subprocess
import tempfile
from enum import Enum

from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel


class RunCode(BaseModel):
    code: str
    input: str


class RunStatus(str, Enum):
    SUCCESS = "success"
    COMPILE_ERROR = "compile_error"
    RUNTIME_ERROR = "runtime_error"
    TIME_LIMIT_EXCEED = "time_limit_exceed"


TIMEOUT = 8

app = FastAPI()


@app.post("/")
def run(run_code: RunCode, background_tasks: BackgroundTasks):
    try:
        compile(run_code.code, "string", "exec")
    except Exception as e:
        return {"status": RunStatus.COMPILE_ERROR, "output": str(e).encode().hex()}

    temp_file = tempfile.mktemp()

    with open(temp_file, "w") as f:
        f.write(run_code.code)

    proc = subprocess.Popen(
        [
            "nsjail",
            "-Q",
            "--config",
            "/home/user/nsjail.cfg",
            "-R",
            f"{temp_file}:/home/user/run.py",
            "--",
            "/usr/bin/python3",
            "/home/user/run.py",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        stdout, stderr = proc.communicate(run_code.input.encode(), timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        proc.kill()
        os.remove(temp_file)
        return {"status": RunStatus.TIME_LIMIT_EXCEED, "output": ""}

    background_tasks.add_task(os.remove, temp_file)

    if proc.returncode == 0:
        return {"status": RunStatus.SUCCESS, "output": stdout.hex()}
    return {"status": RunStatus.RUNTIME_ERROR, "output": stderr.hex()}
