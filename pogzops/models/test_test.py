"""This is only used as a prototyping use of pydantic"""
from typing import List
from pydantic import BaseModel, ValidationError
import pytest
from pogzops.models.status import Status, Success


class MyCopyOperation(BaseModel):
    id: List[str]
    source_env: str
    target_env: str

    def execute(self) -> Status:
        return Success(999)


def test_validation():
    input_copy_op_with_missing_target_env = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [
            {
                "name": "fake_operation_name",
                "id": [""],
                "source_env": "",
            }
        ],
    }
    with pytest.raises(ValidationError):
        MyCopyOperation(**input_copy_op_with_missing_target_env["ops"][0])
