from json import dumps
import logging
from enum import Enum
from operator import add, mul, sub, truediv
from random import random
from time import sleep

from pydantic import BaseModel

LOGGER = logging.getLogger(__name__)


class OperationType(Enum):

    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"


class Operation(BaseModel):

    operation_type: OperationType
    value: float

    def __repr__(self) -> str:
        return dumps(
            {
                "type": self.operation_type.value,
                "value": self.value,
            }
        )


class Multiplexer:

    MAPPING_OPERATIONS = {
        OperationType.ADD: add,
        OperationType.SUB: sub,
        OperationType.MUL: mul,
        OperationType.DIV: truediv,
    }

    def __init__(self) -> None:

        self.__hold = 0

    def operate(self, operation: Operation):

        try:
            sleep(random() / 100)
            self.__hold = self.MAPPING_OPERATIONS[operation.operation_type](
                self.__hold,
                operation.value,
            )
            LOGGER.info(f"operate successfully: {operation!r}")
        except ZeroDivisionError:
            LOGGER.warning("zero division encountered")
