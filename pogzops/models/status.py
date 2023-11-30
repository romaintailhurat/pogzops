from dataclasses import dataclass
from pogzops.models.types import Payload


@dataclass
class Status:
    status_code: int
    payload: Payload = None  # most of the time a JSON questionnaire

    def is_success(self):
        return type(self) is Success


@dataclass
class Success(Status):
    pass


@dataclass
class Failure(Status):
    pass
