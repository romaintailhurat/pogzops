import json
from pydantic import BaseModel
from pogzops.models.envs import PoguesEnv
from pogzops.models.status import (
    Failure,
    OperationFailure,
    OperationPartial,
    OperationStatus,
    OperationSuccess,
    Status,
    Success,
)
from pogzops.remote.opz import change_stamp, copy
from pogzops.remote.get import get_questionnaire
import abc

implemented_operations = {
    "change_stamp": "Set a new value for the target questionnaire stamp.",
    "check_existence": "Check if a questionnaire exists in a target environment.",
    "download": "",
}


def choose_operation_status(statuses: list[Status]) -> OperationStatus:
    """Choose the `OperationStatus` from the list of statuses"""
    if all([type(status) is Success for status in statuses]):
        return OperationSuccess(statuses)
    elif all([type(status) is Failure for status in statuses]):
        return OperationFailure(statuses)
    else:
        return OperationPartial(statuses)


class Operation(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> OperationStatus:
        raise NotImplementedError(
            "This is an abstract method that must be implemented."
        )


class ChangeStamp(BaseModel, Operation):
    """Change the stamp of some questionnaires"""

    type: str
    ids: list[str]
    stamp: str
    source_env: PoguesEnv

    def execute(self) -> OperationStatus:
        statuses = []
        for id in self.ids:
            statuses.append(change_stamp(id, self.stamp, self.source_env))
        return choose_operation_status(statuses)


class CheckExistence(BaseModel, Operation):
    """Check if a questionnaire exists"""

    type: str
    ids: list[str]
    source_env: PoguesEnv

    def __str__(self):
        return "CheckExistence Operation"

    def execute(self) -> OperationStatus:
        statuses = []
        for id in self.ids:
            statuses.append(get_questionnaire(id, self.source_env))
        return choose_operation_status(statuses)


class Copy(BaseModel, Operation):
    """Copy a questionnaire from a source env to a target env"""

    type: str
    ids: list[str]
    source_env: PoguesEnv
    target_env: PoguesEnv

    def execute(self) -> OperationStatus:
        statuses = []
        for id in self.ids:
            statuses.append(copy(id, self.source_env, self.target_env))
        return choose_operation_status(statuses)


class Download(BaseModel, Operation):
    """Download questionnaires"""

    type: str
    ids: list[str]
    source_env: PoguesEnv

    def execute(self) -> OperationStatus:
        statuses = []
        for id in self.ids:
            status = get_questionnaire(id, self.source_env)
            statuses.append(status)
            with open(f"{id}.json", "w", encoding="UTF-8") as json_file:
                json.dump(status.payload, json_file, ensure_ascii=False)
        return OperationSuccess(statuses)


class OperationNotImplemented(Operation):
    def execute(self) -> OperationStatus:
        return OperationFailure(None)
