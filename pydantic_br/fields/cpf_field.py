from typing import Any, Callable, Dict, Generator

from ..field_erros import (
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)
from ..validators.cpf_validator import CPFValidator

__all__ = [
    "CPF",
    "CPFMask",
    "CPFDigits",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class CPFBase(str):
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
        cpf = CPFValidator(value)
        if not cpf.validate():
            raise FieldInvalidError()
        return value


class CPF(CPFBase):
    """
    Accepts string of CPF with or without mask.

    Attributes:
        number (str): CPF number.
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate


class CPFMask(CPFBase):
    """
    Only Accepts string of CPF with mask.

    Attributes:
        number (str): CPF number.
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_mask
        yield cls.validate

    @classmethod
    def validate_mask(cls, value: str) -> str:
        cpf = CPFValidator(value)
        if not cpf.validate_mask():
            raise FieldMaskError()
        return value


class CPFDigits(CPFBase):
    """
    Only Accepts string of CPF with digits.

    Attributes:
        number (str): CPF number.
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
