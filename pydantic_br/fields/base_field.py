from typing import Any, Callable, Dict, Generator

from ..field_erros import (
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)
from ..get_versions import get_pydantic_version
from ..validators.base_validator import FieldMaskValidator, FieldValidator
from .base_field_v2 import BaseDigitsV2, BaseMaskV2, BasePydanticV2

__all__ = [
    "Base",
    "BaseMask",
    "BaseDigits",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]

pydantic_version = get_pydantic_version()


class Base(BasePydanticV2):
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
            if pydantic_version.value == 1:
                raise FieldTypeError()
            if pydantic_version.value == 2:
                raise FieldTypeError(FieldTypeError.msg_template)
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        doc = cls.Validator(value)
        if not doc.validate():
            if pydantic_version.value == 1:
                raise FieldInvalidError()
            if pydantic_version.value == 2:
                raise FieldInvalidError(FieldInvalidError.msg_template)
        return value


class BaseMask(Base, BaseMaskV2):
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
            if pydantic_version.value == 1:
                raise FieldMaskError()
            if pydantic_version.value == 2:
                raise FieldMaskError(FieldMaskError.msg_template)
        return value


class BaseDigits(Base, BaseDigitsV2):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            if pydantic_version.value == 1:
                raise FieldDigitError()
            if pydantic_version.value == 2:
                raise FieldDigitError(FieldDigitError.msg_template)
        return value
