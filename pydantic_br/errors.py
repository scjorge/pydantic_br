from typing import Any


class PydanticErrorMixin:
    code: str
    msg_template: str

    def __init__(self, **ctx: Any) -> None:
        self.__dict__ = ctx

    def __str__(self) -> str:
        return self.msg_template.format(**self.__dict__)


class PydanticValueError(PydanticErrorMixin, ValueError):
    ...


class PydanticTypeError(PydanticErrorMixin, TypeError):
    ...


class FieldMaskNumberError(PydanticTypeError):
    msg_template = "you can not set force_mask and force_numbers as True togheter"


class CPFError(PydanticValueError):
    msg_template = "invalid CPF"


class CPFTypeError(PydanticTypeError):
    msg_template = "the CPF field only accepts string"


class CPFMaskError(PydanticValueError):
    msg_template = "invalid Mask CPF format"


class CPFDigitError(PydanticValueError):
    msg_template = "CPF filds only accept digits"
