from typing import TYPE_CHECKING

from ..utils import get_pydantic_type_error

__all__ = [
    "FieldMaskNumberError",
]

if TYPE_CHECKING:

    class PydanticTypeError(TypeError):
        ...

else:
    PydanticTypeError = get_pydantic_type_error()


class FieldMaskNumberError(PydanticTypeError):
    msg_template = "you can not set force_mask and force_numbers as True togheter"
