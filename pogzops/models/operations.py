from dataclasses import dataclass
from pogzops.models.envs import PoguesEnv
from pogzops.models.types import Stamp
from pogzops.models.status import Status, Failure
from pogzops.remote.opz import change_stamp
from pogzops.remote.get import get_questionnaire
import abc


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


"""
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
"""


@dataclass
class Operation(abc.ABC):
    name: str
    env: PoguesEnv

    @abc.abstractmethod
    def execute(self) -> Status:
        raise NotImplementedError(
            "This is an abstract method that must be implemented."
        )


@dataclass
class ChangeStamp(Operation):
    params: SingleQuestionnaireParams

    def execute(self) -> Status:
        return change_stamp(self.params.id, self.params.stamp, self.env)


@dataclass
class CheckExistence(Operation):
    params: SingleQuestionnaireParams

    def execute(self) -> Status:
        return get_questionnaire(self.params.id, self.env)


@dataclass
class OperationNotImplemented(Operation):
    def execute(self) -> Status:
        return super().execute()
