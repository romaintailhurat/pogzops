from pogzops.input.read_opz import generate_operations_from_yaml
from pogzops.models.operations import OperationNotImplemented


def test_bad_yaml():
    pass


def test_not_implemented_operation():
    input_with_not_implemented_operation = {
        "envs": [{"env": "", "url": "", "name": "", "token": ""}],
        "ops": [{"name": "fake_operation_name", "env": ""}],
    }
    operations = generate_operations_from_yaml(input_with_not_implemented_operation)
    assert type(operations[0]) is OperationNotImplemented
