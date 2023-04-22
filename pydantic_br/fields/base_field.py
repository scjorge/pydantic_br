from typing import Any, Callable, Dict, Generator

from ..field_erros import (
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)
from ..validators.base_validator import FieldMaskValidator, FieldValidator

__all__ = [
    "Base",
    "BaseMask",
    "BaseDigits",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class Base:
    format: str
    Validator: Callable[..., FieldValidator]

    __slots__ = ["number"]

    def __init__(self, number: str) -> None:
        self.number = number

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format=cls.format)

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate

    @classmethod
    def validate_type(cls, value: str) -> str:
        if not isinstance(value, str):
            raise FieldTypeError()
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        doc = cls.Validator(value)
        if not doc.validate():
            raise FieldInvalidError()
        return value


class BaseMask(Base):
    Validator: Callable[..., FieldMaskValidator]

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_mask
        yield cls.validate

    @classmethod
    def validate_mask(cls, value: str) -> str:
        doc = cls.Validator(value)
        if not doc.validate_mask():
            raise FieldMaskError()
        return value


class BaseDigits(Base):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            raise FieldDigitError()
        return value
