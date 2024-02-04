from pydantic import ValidationError
from pogzops.models.operations import (
    Copy,
    OperationNotImplemented,
    ChangeStamp,
    SingleQuestionnaireParams,
)
from pogzops.models.envs import PoguesEnv
import pytest

test_env = PoguesEnv("test_env", "http://no.where")


def test_not_implemented_operation():
    noop = OperationNotImplemented("noop", test_env)
    with pytest.raises(NotImplementedError):
        noop.execute()


def test_operation_str_rep():
    cs_name = "test_change_stamp"
    params = SingleQuestionnaireParams("testid", "NEW_STAMP")
    change_stamp_op = ChangeStamp(cs_name, test_env, params)
    assert (
        str(change_stamp_op)
        == "Changing stamp of questionnnaire testid to NEW_STAMP on env test_env"
    )


def test_copy_with_bad_params():
    input_copy_op_with_missing_target_env = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "id": "", "source_env": ""}],
    }
    input_copy_op_with_missing_source_env = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "id": "", "target_env": ""}],
    }
    input_copy_op_with_missing_id = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "source_env": "", "target_env": ""}],
    }
    input_copy_op_with_empty_id = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [
            {
                "name": "fake_operation_name",
                "id": [""],
                "source_env": "",
                "target_env": "",
            }
        ],
    }
    with pytest.raises(ValidationError):
        Copy(**input_copy_op_with_empty_id["ops"][0])
