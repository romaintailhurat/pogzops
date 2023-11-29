from dataclasses import dataclass


@dataclass
class OperationParams:
    pass


@dataclass
class SingleQuestionnaireParams(OperationParams):
    id: str
    stamp: str | None = None


@dataclass
class Operation:
    name: str
    params: OperationParams

    def execute(self):
        # choose operations from from pogzops.remote.opz for example
        # then execute
        # return Status ?
        print(f"Operation {self.name} execution - to be implemented")
