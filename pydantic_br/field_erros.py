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


class CPFInvalidError(PydanticValueError):
    msg_template = "invalid CPF"


class CPFTypeError(PydanticTypeError):
    msg_template = "the CPF field only accepts string"


class CPFMaskError(PydanticValueError):
    msg_template = "invalid Mask CPF format"


class CPFDigitError(PydanticValueError):
    msg_template = "CPF filds only accept digits"


class CNPJInvalidError(PydanticValueError):
    msg_template = "invalid CNPJ"


class CNPJTypeError(PydanticTypeError):
    msg_template = "the CNPJ field only accepts string"


class CNPJMaskError(PydanticValueError):
    msg_template = "invalid Mask CNPJ format"


class CNPJDigitError(PydanticValueError):
    msg_template = "CNPJ filds only accept digits"
