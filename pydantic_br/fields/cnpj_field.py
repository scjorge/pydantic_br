from typing import Any, Callable, Dict, Generator

from ..field_erros import (
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)
from ..validators.cnpj_validator import validate_cnpj, validate_cnpj_mask

__all__ = [
    "CNPJ",
    "CNPJMask",
    "CNPJDigits",
]


AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class CNPJBase(str):
    __slots__ = ["number"]

    def __init__(self, number: str) -> None:
        self.number = number

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format="cpf")

    @classmethod
    def validate_type(cls, value: str) -> str:
        if not isinstance(value, str):
            raise FieldTypeError()
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        if not validate_cnpj(value):
            raise FieldInvalidError()
        return value


class CNPJ(CNPJBase):
    """
    Accepts string of CNPJ with or without mask.

    Attributes:
        number (str): CNPJ number.
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate


class CNPJMask(CNPJBase):
    """
    Only Accepts string of CNPJ with mask.

    Attributes:
        number (str): CNPJ number.
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_mask
        yield cls.validate

    @classmethod
    def validate_mask(cls, value: str) -> str:
        if not validate_cnpj_mask(value):
            raise FieldMaskError()
        return value


class CNPJDigits(CNPJBase):
    """
    Only Accepts string of CNPJ with digits.

    Attributes:
        number (str): CNPJ number.
    """

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
