from pogzops.models.operations import (
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
