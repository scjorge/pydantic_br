from typing import Any, Callable, Dict, Generator

from ..validators.base_validator import FieldMaskValidator, FieldValidator
from .base_field_class import BaseFieldClass

__all__ = [
    "Basev1",
    "BaseMaskv1",
    "BaseDigitsv1",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class Basev1(BaseFieldClass):
    Validator: Callable[..., FieldValidator]

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(
            type="string", format=cls.format, mask=cls.mask, example=cls.examples
        )

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate


class BaseMaskv1(Basev1):
    Validator: Callable[..., FieldMaskValidator]

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_mask
        yield cls.validate


class BaseDigitsv1(Basev1):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate
