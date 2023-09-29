from dataclasses import dataclass

@dataclass
class Status:
    status_code: int
    payload: dict = None # most of the time a JSON questionnaire

@dataclass
class Success(Status):
    pass

@dataclass
class Failure(Status):
    pass