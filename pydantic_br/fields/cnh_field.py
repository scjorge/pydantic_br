from typing import Any, Callable, Dict, Generator

from ..field_erros import FieldDigitError, FieldInvalidError, FieldTypeError
from ..validators.cnh_validator import CNHValidator

__all__ = ["CNH"]


AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class CNH(str):
    __slots__ = ["number"]

    def __init__(self, number: str) -> None:
        self.number = number

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format="cnh")

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate

    @classmethod
    def validate_type(cls, value: str) -> str:
        if not isinstance(value, str):
            raise FieldTypeError()
        return value

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            raise FieldDigitError()
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        cnh = CNHValidator(value)
        if not cnh.validate():
            raise FieldInvalidError()
        return value
