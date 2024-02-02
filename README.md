# 🛴 pogzops 🛴

__pogzops__ is a set of Python programs that helps a Pogues power user with several tasks.

> WIP use as a cli and as a set of programs

## Use cases

### Using the CLI

Currently:

`$> poetry run pgz exe pogzops\example-command.yaml`

We're targeting to use `pogzops` as a Python cli:

`$> pogzops exe my-operations.yaml`

The YAML file has this structure:

```yaml
ops:
  - name: "change_stamp"
    type: "single"
    id: "lpjqty81"
    stamp: "TEST"
    env: "demo"
envs:
  - env: "demo"
    url: "https://api-conception-questionnaires.demo.insee.io"
    name: "demo"
    token: ""
```

ops contains a list of operations, envs is a list of Pogues envs (the API).

You can use `$> poetry run pgz ls` to get the list of available operations.

### Using the lib

For example, a power user might like to copy several questionnaires from one environment to another:

```python
from remote.opz import copy
from models.envs import PoguesEnv

first_env = PoguesEnv("first", envs["first"])
second_env = PoguesEnv("second", envs["second"])

questionnaires_ids = ["lkuyylbx", "lj7683a6"]

for id in questionnaires_ids:
    copy(id, first_env, second_env)
```

## How to run?

The package management is handled by [poetry](https://python-poetry.org/), that need to be installed beforehand.

Then, the easiest way to run a program will be to launch the `run.py` file with the appropriate code, using this command at the root of `pogzops` directory:

`$> poetry run python pogzops/run.py`

## Lint

`$> poetry run ruff check .`

See [ruff](https://github.com/astral-sh/ruff).

## TODO

- [ ] build a proper lib :v:
- [ ] `cert_path` → boolean or Path ?
  - [ ] handle path to certificate from the yaml file
- [ ] `no_proxy` (currently handled in terminal by `set no_proxy=<domain.com>`
- [ ] handle time out exceptions (or other type of exception resulting from a non terminating HTTP exchange)
- [ ] proper cli build, see [this](https://dev.to/bowmanjd/build-command-line-tools-with-python-poetry-4mnc)
