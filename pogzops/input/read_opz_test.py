from pogzops.input.read_opz import generate_operations_from_yaml
from pogzops.models.operations import OperationNotImplemented
import pytest


def test_bad_yaml():
    pass


def test_not_implemented_operation():
    input_with_not_implemented_operation = {
        "envs": [{"env": "", "url": "", "name": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "source_env": ""}],
    }
    operations = generate_operations_from_yaml(input_with_not_implemented_operation)
    assert type(operations[0]) is OperationNotImplemented


def test_badly_formated_env():
    input_env_with_missing_name = {
        "envs": [{"env": "", "url": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "env": ""}],
    }
    input_env_with_missing_url = {
        "envs": [{"env": "", "name": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "env": ""}],
    }
    with pytest.raises(RuntimeError):
        generate_operations_from_yaml(input_env_with_missing_name)
    with pytest.raises(RuntimeError):
        generate_operations_from_yaml(input_env_with_missing_url)


def test_badly_formated_op():
    input_ops_with_missing_source_env = {
        "envs": [{"env": "", "name": "", "url": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "env": ""}],
    }

    with pytest.raises(RuntimeError):
        generate_operations_from_yaml(input_ops_with_missing_source_env)
