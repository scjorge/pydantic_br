from typing import TYPE_CHECKING

from ..utils import get_pydantic_type_error, get_pydantic_value_error

__all__ = [
    "CPFError",
    "CPFTypeError",
    "CPFMaskError",
    "CPFDigitError",
]

if TYPE_CHECKING:

    class PydanticValueError(ValueError):
        ...

    class PydanticTypeError(TypeError):
        ...

else:
    PydanticValueError = get_pydantic_value_error()
    PydanticTypeError = get_pydantic_type_error()


class CPFError(PydanticValueError):
    # code = "none.not_allowed"
    msg_template = "invalid CPF"


class CPFTypeError(PydanticTypeError):
    # code = "none.not_allowed"
    msg_template = "the CPF field only accepts string"


class CPFMaskError(PydanticValueError):
    # code = "none.not_allowed"
    msg_template = "invalid Mask CPF format"


class CPFDigitError(PydanticValueError):
    # code = "none.not_allowed"
    msg_template = "CPF filds only accept digits"
