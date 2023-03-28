from ..utils import get_pydantic_type_error, get_pydantic_value_error

__all__ = ["CPFValueError", "CPFTypeError"]


PydanticValueError = get_pydantic_value_error()
PydanticTypeError = get_pydantic_type_error()


class CPFValueError(PydanticValueError):
    # code = "none.not_allowed"
    msg_template = "invalid CPF format"


class CPFTypeError(PydanticTypeError):
    # code = "none.not_allowed"
    msg_template = "the cpf field only accepts string"
