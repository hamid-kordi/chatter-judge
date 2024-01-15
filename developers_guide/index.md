# Welcome Contributors

## Collaboration Guidelines
### Forking this Repository:

Fork the [`chatter-judge`](https://github.com/1chooo/chatter-judge) repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/chatter-judge.git
```

### Setting Upstream Remote:
```shell
$ git remote add upstream git@github.com:1chooo/chatter-judge.git

$ git remote -v
origin  git@github.com:<your_user_name>/chatter-judge.git (fetch)
origin  git@github.com:<your_user_name>/chatter-judge.git (push)
upstream        git@github.com:1chooo/chatter-judge.git (fetch)
upstream        git@github.com:1chooo/chatter-judge.git (push)
```
### Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:
If you encounter any problems while contributing to this project, please report the issues in the [chatter-judge/issues](https://github.com/1chooo/chatter-judge/issues) section.

### Important Notes:

#### Make sure to synchronize and update your repository before initiating a pull request:

1. Run `git stash save` to temporarily stash your local changes.
2. Run `git fetch upstream` to sync the source project with your local copy.
3. Run `git checkout main` to switch to the main branch.
4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.

## Developing Requirements

Python version `python3.10` or later.

### Build `venv` for **MacOS**
```shell
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

### Run web app
```shell
$ ./build.sh

# or
$ uvicorn run:main --host 127.0.0.1 --port 5002
```

### Build Docs
```shell
$ mkdocs server
$ mkdocs build
```
