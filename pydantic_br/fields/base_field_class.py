from typing import Any, Callable, Generator

from .base_field_errors import FieldTypes, raise_field

__all__ = ["BaseFieldClass"]


AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class BaseFieldClass:
    format: str
    Validator: Callable[..., Any]

    __slots__ = ["number"]

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

    @classmethod
    def validate_mask(cls, value: str) -> str:
        doc = cls.Validator(value)
        if not doc.validate_mask():
            raise_field(FieldTypes.mask)
        return value

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            raise_field(FieldTypes.digit)
        return value
