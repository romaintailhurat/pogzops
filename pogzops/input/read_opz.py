"""
Read and parse the cli opz yaml file.
"""
from pathlib import Path
from yaml import safe_load
from pogzops.models.operations import (
    Copy,
    Download,
    Operation,
    ChangeStamp,
    CheckExistence,
    OperationNotImplemented,
)


def check_input_op(input_op: dict) -> bool:
    ok_source_env = "source_env" in input_op.keys()
    return ok_source_env


def generate_operations_from_yaml(raw_yaml) -> list[Operation]:
    """Generate the list of `Operation` from the source input."""

    ops: list[Operation] = []
    for op in raw_yaml["ops"]:
        if check_input_op(op) is False:
            raise RuntimeError("bad op format")
        match op["type"]:
            case "change_stamp":
                ops.append(ChangeStamp(**op))
            case "check_existence":
                ops.append(
                    CheckExistence(**op),
                )

            case "copy":
                ops.append(
                    Copy(**op),
                )

            case "download":
                ops.append(Download(**op))

            case _:
                ops.append(OperationNotImplemented())
    return ops


def read_opz_file(path_to_yaml: Path) -> list[Operation]:
    """Instanciate environments (`envs`) and operations (`ops`) from a yaml source file."""
    with open(path_to_yaml) as opz_yaml:
        raw_yaml = safe_load(opz_yaml)
        return generate_operations_from_yaml(raw_yaml)
