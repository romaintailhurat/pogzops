from dataclasses import dataclass
from pogzops.models.envs import PoguesEnv
from pogzops.models.types import Stamp
from pogzops.models.status import Status, Failure
from pogzops.remote.opz import change_stamp


@dataclass
class OperationParams:
    pass


@dataclass
class SingleQuestionnaireParams(OperationParams):
    id: str
    stamp: Stamp


@dataclass
class MultiQuestionnairesParams(OperationParams):
    ids: list[str]


@dataclass
class Operation:
    name: str
    env: PoguesEnv
    params: SingleQuestionnaireParams

    def execute(self) -> Status:
        # choose operations from from pogzops.remote.opz for example
        # then execute
        # return Status ?
        match self.name:
            case "change_stamp":
                status = change_stamp(self.params.id, self.params.stamp, self.env)
                print(status)
                return status
            case _:
                print(f"Operation {self.name} execution - to be implemented")
                return Failure(999)
