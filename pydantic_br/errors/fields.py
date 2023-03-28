from ..utils import get_pydantic_type_error

__all__ = [
    "FieldMaskNumberError",
]

PydanticTypeError = get_pydantic_type_error()


class FieldMaskNumberError(PydanticTypeError):
    msg_template = "you can not set force_mask and force_numbers as True togheter"
