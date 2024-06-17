FROM ubuntu:22.04 as chroot

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apt/*
RUN /usr/sbin/useradd --no-create-home -u 1000 user && \
    mkdir -vp /home/user

FROM gcr.io/kctf-docker/challenge@sha256:501458c0426acc3b5a74a661791271faf0dca6555b46bfb76f944d2558bd08d5

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip && \
    pip install --no-cache-dir fastapi uvicorn && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/user

COPY nsjail.cfg /home/user/
RUN chmod 644 /home/user/nsjail.cfg

COPY --from=chroot / /chroot

COPY app.py /home/user/

CMD uvicorn app:app --host 0.0.0.0 --port 1337
