from typing import Any, Callable, Dict, Generator

from .errors import (
    CPFDigitError,
    CPFError,
    CPFMaskError,
    CPFTypeError,
    FieldMaskNumberError,
)
from .validators import validate_cpf, validate_cpf_mask

__all__ = [
    "CPF",
    "CPFMask",
    "CPFDigits",
    "FieldBR",
]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]


class FieldBR:
    def __init__(
        self, default: Any, *, force_mask: bool = False, force_numbers: bool = False
    ) -> Any:
        self.default = default
        if force_mask and force_numbers:
            raise FieldMaskNumberError()

        settings = [
            ("force_mask", force_mask),
            ("force_numbers", force_numbers),
        ]

        for setting in settings:
            if setting[0] in dir(default):
                setattr(default, setting[0], setting[1])
        # return default

    def f(self: Any) -> Any:
        return self.default


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
    def validate_mask(cls, value: str) -> str:
        if not validate_cpf_mask(value):
            raise CPFMaskError()
        return value

    @classmethod
    def validate_numbers(cls, value: str) -> str:
        if not value.isdigit():
            raise CPFDigitError()
        return value

    @classmethod
    def validate(cls, value: str) -> str:
        if not validate_cpf(value):
            raise CPFError()
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


class CPFDigits(CPFBase):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate_type
        yield cls.validate_numbers
        yield cls.validate
