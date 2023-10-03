# 🛴 pogzops 🛴

__pogzops__ is a set of Python programs that helps a Pogues power user with several tasks.

## Use cases

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

# TODO

- [ ] build a proper lib :v:
- [ ] `cert_path` → boolean or Path ?
- [ ] `no_proxy` (currently handled in terminal by `set no_proxy=<domain.com>`
- [ ] handle time out exceptions (or other type of exception resulting from a non terminating HTTP exchange)
