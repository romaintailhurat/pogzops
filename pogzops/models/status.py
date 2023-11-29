from dataclasses import dataclass


@dataclass
class Status:
    status_code: int
    payload: dict | None = None  # most of the time a JSON questionnaire

    def is_success(self):
        return type(self) is Success


@dataclass
class Success(Status):
    pass


@dataclass
class Failure(Status):
    pass
