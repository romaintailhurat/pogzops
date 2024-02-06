from dataclasses import dataclass
import stat
from typing import List

from pydantic import BaseModel
from pogzops.models.envs import PoguesEnv
from pogzops.models.types import Stamp
from pogzops.models.status import (
    Failure,
    OperationFailure,
    OperationPartial,
    OperationStatus,
    OperationSuccess,
    Status,
    Success,
)
from pogzops.remote.opz import change_stamp
from pogzops.remote.get import get_questionnaire
import abc

implemented_operations = {
    "change_stamp": "Set a new value for the target questionnaire stamp.",
    "check_existence": "Check if a questionnaire exists in a target environment.",
}


@dataclass
class OperationParams:
    pass


@dataclass
class SingleQuestionnaireParams(OperationParams):
    id: str
    stamp: Stamp = None


@dataclass
class MultiQuestionnairesParams(OperationParams):
    ids: list[str]


@dataclass
class Operation(abc.ABC):
    name: str
    env: PoguesEnv

    @classmethod
    @abc.abstractmethod
    def check_operation_params(cls, operations_params: dict) -> bool:
        raise NotImplementedError(
            "This is an abstract method that must be implemented."
        )

    @abc.abstractmethod
    def execute(self) -> Status:
        raise NotImplementedError(
            "This is an abstract method that must be implemented."
        )


class NewOperation(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> OperationStatus:
        raise NotImplementedError(
            "This is an abstract method that must be implemented."
        )


@dataclass
class ChangeStamp(Operation):
    params: SingleQuestionnaireParams

    def __str__(self) -> str:
        return f"Changing stamp of questionnnaire {self.params.id} to {self.params.stamp} on env {self.env.name}"

    @classmethod
    def check_operation_params(cls, operation_params: dict):
        """Checking the YAML params for this operation"""
        # TODO to be implemented
        return False

    def execute(self) -> Status:
        return change_stamp(self.params.id, self.params.stamp, self.env)


class CheckExistence(BaseModel):
    """Check if a questionnaire exists"""

    name: str
    ids: List[str]
    source_env: PoguesEnv

    def execute(self) -> OperationStatus:
        statuses = []
        for id in self.ids:
            statuses.append(get_questionnaire(id, self.source_env))
        if all([type(status) is Success for status in statuses]):
            return OperationSuccess(statuses)
        elif all([type(status) is Failure for status in statuses]):
            return OperationFailure(statuses)
        else:
            return OperationPartial(statuses)


class Copy(BaseModel):
    """Copy a questionnaire from a source env to a target env"""

    name: str
    id: List[str]
    source_env: PoguesEnv
    target_env: PoguesEnv

    def execute(self) -> Status:
        raise NotImplementedError("WIP")


@dataclass
class OperationNotImplemented(Operation):
    @classmethod
    def check_operation_params(cls, operations_params: dict) -> bool:
        return False

    def execute(self) -> Status:
        return super().execute()
