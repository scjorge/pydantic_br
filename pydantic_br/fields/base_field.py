from typing import Any, Callable, Dict, Generator

from ..field_errors import FieldTypes, raise_field
from ..validators.base_validator import FieldMaskValidator, FieldValidator
from .base_field_v2 import BaseDigitsV2, BaseMaskV2, BasePydanticV2

__all__ = [
    "Base",
    "BaseMask",
    "BaseDigits",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class Base(BasePydanticV2):
    format: str
    Validator: Callable[..., FieldValidator]

    __slots__ = ["number"]

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format=cls.format)

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate

    @classmethod
    def validate_type(cls, value: Any) -> str:
        if not isinstance(value, str):
            raise_field(FieldTypes.type)
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        doc = cls.Validator(value)
        if not doc.validate():
            raise_field(FieldTypes.invalid)
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
            raise_field(FieldTypes.mask)
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
            raise_field(FieldTypes.digit)
        return value
