"""
Read and parse the cli opz yaml file.
"""
from pathlib import Path
from yaml import safe_load
from pogzops.models.envs import PoguesEnv
from pogzops.models.operations import Operation, SingleQuestionnaireParams


def read_opz_file(path_to_yaml: Path) -> list[Operation]:
    with open(path_to_yaml) as opz_yaml:
        raw_yaml = safe_load(opz_yaml)
        envs = {
            env["name"]: PoguesEnv(env["name"], env["url"]) for env in raw_yaml["envs"]
        }
        ops = []
        stamp = None
        # TODO spaghetti code :(
        for op in raw_yaml["ops"]:
            if "stamp" in op:
                stamp = op["stamp"]
            ops.append(
                Operation(
                    op["name"],
                    envs[op["env"]],
                    SingleQuestionnaireParams(op["id"], stamp),
                )
            )
        return ops
