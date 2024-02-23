# 🛴 pogzops 🛴

__pogzops__ is a command line helping with management tasks over Pogues environments.

For example if i want to download some questionnaires, i can use the following command:

`$> pgz exe my-download-command.yaml`

With the YAML file being:

```yaml
ops:
  - type: "download"
    ids:
      - "abcdef12"
      - "ghij45kl"
    source_env:
      name: "pogues"
      url: "https://my-pogues-api.example.com"
```

The `ops` array will handle the different operations you want to achieve. For every operation, you need to detail:

- the `type` of the operation
  - the `pgz ls` command will give you the list, see also the doc below ;)
- the `ids` of the questionnaire involved
  - can be 1 but no less
- the source Pogues environment `source_env` which contains the `url` of the Pogues API we want to query

Other elements could be necessary depending of the type of operations (more on that below).

### More on envs

> WIP

## How to run?

The package management is handled by [poetry](https://python-poetry.org/), that need to be installed beforehand.

Then, the easiest way to run a program will be to launch the `run.py` file with the appropriate code, using this command at the root of `pogzops` directory:

`$> poetry run python pogzops/run.py`

In an near future, pogzops will be available as a python lib.

## List of operations

### Copy a questionnaire from one environment to the other

Will create or update a questionnaire in a target environment from the questionnaire model in a source environment.

```yaml
ops:
  - type: "copy"
    ids:
      - "quest0001"
      - "quest0002"
      - "quest0003"
      - "quest0004"
    source_env:
      name: "origin"
      url: "https://origin-api.example.com"
      token: "my-identification-token"
    target_env:
      name: "sandbox"
      url: "https://sanbox-api.there.com"
```

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
