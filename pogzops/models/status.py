from dataclasses import dataclass
from typing import List
from pogzops.models.types import Payload


@dataclass
class Status:
    status_code: int | None = None
    message: str | None = None
    payload: Payload = None  # most of the time a JSON questionnaire

    def is_success(self):
        return type(self) is Success


@dataclass
class Success(Status):
    pass


@dataclass
class Failure(Status):
    pass


@dataclass
class OperationStatus:
    source_statuses: List[Status] | None


@dataclass
class OperationSuccess(OperationStatus):
    pass


@dataclass
class OperationPartial(OperationStatus):
    pass


@dataclass
class OperationFailure(OperationStatus):
    pass
