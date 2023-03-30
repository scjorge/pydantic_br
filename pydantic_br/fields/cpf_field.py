from typing import Any, Callable, Dict, Generator

from ..errors.cpf_erros import (
    CPFDigitError,
    CPFInvalidError,
    CPFMaskError,
    CPFTypeError,
)
from ..validators.cpf_validator import validate_cpf, validate_cpf_mask

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
            raise CPFTypeError()
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        if not validate_cpf(value):
            raise CPFInvalidError()
        return value


class CPF(CPFBase):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate


class CPFMask(CPFBase):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_mask
        yield cls.validate

    @classmethod
    def validate_mask(cls, value: str) -> str:
        if not validate_cpf_mask(value):
            raise CPFMaskError()
        return value


class CPFDigits(CPFBase):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            raise CPFDigitError()
        return value
