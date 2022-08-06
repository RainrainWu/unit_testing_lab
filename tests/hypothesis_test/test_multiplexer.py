from math import nan
from hypothesis import given, example, assume, event
from hypothesis.strategies import builds
from unit_testing_lab.multiplexer import Multiplexer, Operation, OperationType


class TestMultiplexer:

    sampler_operation = builds(Operation)

    @given(operation=sampler_operation)
    @example(Operation(operation_type=OperationType.DIV, value=0.0))
    @example(Operation(operation_type=OperationType.DIV, value=nan))
    def test_operate(self, operation):

        event(f"is_nan: {operation.value == nan}")
        Multiplexer().operate(operation)

    @given(
        operation=sampler_operation.filter(
            lambda op: op.operation_type == OperationType.ADD
        )
    )
    def test_operate_add_only(self, operation):

        Multiplexer().operate(operation)

    @given(
        operation=sampler_operation.filter(
            lambda op: op.operation_type == OperationType.ADD
        )
    )
    def test_operate_add_only(self, operation):

        Multiplexer().operate(operation)

    @given(operation=sampler_operation)
    def test_operate_ignore_mul(self, operation):

        assume(operation.operation_type != OperationType.MUL)
        Multiplexer().operate(operation)
