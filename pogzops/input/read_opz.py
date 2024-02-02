"""
Read and parse the cli opz yaml file.
"""
from pathlib import Path
from yaml import safe_load
from pogzops.models.envs import PoguesEnv
from pogzops.models.operations import (
    Operation,
    SingleQuestionnaireParams,
    ChangeStamp,
    CheckExistence,
    OperationNotImplemented,
)


def generate_operations_from_yaml(raw_yaml) -> list[Operation]:
    envs = {env["name"]: PoguesEnv(env["name"], env["url"]) for env in raw_yaml["envs"]}
    ops = []
    stamp = None

    for op in raw_yaml["ops"]:
        match op["name"]:
            case "change_stamp":
                ops.append(
                    ChangeStamp(
                        op["name"],
                        envs[op["env"]],
                        SingleQuestionnaireParams(op["id"], stamp),
                    )
                )
            case "check_existence":
                ops.append(
                    CheckExistence(
                        op["name"],
                        envs[op["env"]],
                        SingleQuestionnaireParams(op["id"], stamp),
                    )
                )
            case _:
                ops.append(OperationNotImplemented(op["name"], envs[op["env"]]))
    return ops


def read_opz_file(path_to_yaml: Path) -> list[Operation]:
    """Instanciate environments (`envs`) and operations (`ops`) from a yaml source file."""
    with open(path_to_yaml) as opz_yaml:
        raw_yaml = safe_load(opz_yaml)
        return generate_operations_from_yaml(raw_yaml)
