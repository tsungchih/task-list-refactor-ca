# Task List Refactor Based On Clean Architecture In Python

This is a side project aimed at refactor of [Task List Kata](https://kata-log.rocks/task-list-kata) based on Clean
Architecture in Python.

## How to set up the development environment?

[Poetry](https://python-poetry.org/) is used in this project for dependency management. Please refer to the
[official site](https://python-poetry.org/docs/) for the various ways to installation. As of proceeding the refactor,
this project used Poetry of version **1.8.5**.

Once we have Poetry installed in your environment. We could clone the project listed as follows.

```shell
$ git clone https://github.com/tsungchih/task-list-refactor-ca.git
```

We can then create a virtual environment and install the project dependencies by means of Poetry.

```shell
$ cd task-list-refactor-ca
$ poetry env use python3.11
$ poetry install
```

Now we can run tests to verify if the virtual environment is successfully set up.

```shell
$ make tests
=> Running pytest
============================= test session starts ==============================
platform darwin -- Python 3.11.10, pytest-8.3.4, pluggy-1.5.0
rootdir: /path/to/task-list-refactor-ca
configfile: pyproject.toml
collected 1 item

tests/test_application.py .                                              [100%]

============================== 1 passed in 0.08s ===============================
==> Running pytest complete
```

We can definitely run `pytest` if the `make` tool is not available in the environment.

```shell
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.11.10, pytest-8.3.4, pluggy-1.5.0
rootdir: /path/to/task-list-refactor-ca
configfile: pyproject.toml
collected 1 item

tests/test_application.py .                                              [100%]

============================== 1 passed in 0.08s ===============================
```

After all, we can enable the virtual environment utilizing the following command.

```shell
$ poetry shell
```

This project relies on [make tool](https://www.gnu.org/software/make/) for automating routine tasks during development.
We may check which targets are currently supported by executing `make` listed as follows.

```shell
$ make

Usage:
  make <target>

Targets:
  help                 Show help information
  build-pkg            Build Python package
  tests                Run pytest to all the packages in the repository
```

The above output showed that three targets, `help`, `build-pkg`, and `tests`, are currently supported. We may add more
targets in the `Makefile` to automate some sorts of routine tasks.

After having successfully set up the development environment, we should prepare the environment for
[pre-commit](https://pre-commit.com/) to work properly.

```shell
$ pre-commit install-hooks
```

We could now run `pre-commit` against the installed hooks using the following command every time we have staged the
changes to the code base.

```shell
$ pre-commit run
check python ast...............................................................Passed
check builtin type constructor use.............................................Passed
check for case conflicts.......................................................Passed
debug statements (python)......................................................Passed
mixed line ending..............................................................Passed
trim trailing whitespace.......................................................Passed
fix end of files...............................................................Passed
check yaml.....................................................................Passed
check json.................................................(no files to check)Skipped
check toml.....................................................................Passed
check for added large files....................................................Passed
detect private key.............................................................Passed
Tests should begin with test_*.py..............................................Passed
check for merge conflicts......................................................Passed
pretty format json.........................................(no files to check)Skipped
don't commit to branch.........................................................Passed
Detect hardcoded secrets.......................................................Passed
apply a consistent format to pyproject.toml files..............................Passed
run 'poetry check' for checking pyproject.toml.................................Passed
run `ruff` for Python linting..................................................Passed
run `ruff format for Python formatting`........................................Passed
run `pyright`, a static type checker...........................................Passed
run 'black' on Python code blocks in documentation files.......................Passed
run 'prettier', an opinionated code formatter..................................Passed
```
