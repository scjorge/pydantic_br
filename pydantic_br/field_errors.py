from enum import Enum

from .get_versions import get_pydantic_version

__all__ = [
    "FieldTypeError",
    "FieldMaskError",
    "FieldDigitError",
    "FieldInvalidError",
    "raise_field",
]


pydantic_version = get_pydantic_version()


class FieldTypes(Enum):
    type = "type"
    mask = "mask"
    digit = "digit"
    invalid = "invalid"


class FieldTypeError:
    code = "not_str"
    msg_template = "Input should be a valid string"
    message_template = msg_template


class FieldMaskError:
    code = "invalid_mask"
    msg_template = "invalid mask format"
    message_template = msg_template


class FieldDigitError:
    code = "not_digits"
    msg_template = "field only accept digits as string"
    message_template = msg_template


class FieldInvalidError:
    code = "invalid_data"
    msg_template = "invalid data"
    message_template = msg_template


def raise_error(code: str, msg_template: str):  # type: ignore
    if pydantic_version.value == 1:
        from pydantic import PydanticTypeError

        PydanticTypeError.code = code
        PydanticTypeError.msg_template = msg_template
        PydanticTypeError.message_template = msg_template
        raise PydanticTypeError()

    if pydantic_version.value == 2:
        from pydantic_core import PydanticCustomError

        PydanticCustomError.code = code
        PydanticCustomError.msg_template = msg_template
        PydanticCustomError.message_template = msg_template
        raise PydanticCustomError(code, msg_template)


def raise_field(context: FieldTypes):
    field_types = {
        FieldTypes.type: (FieldTypeError.code, FieldTypeError.msg_template),
        FieldTypes.mask: (FieldMaskError.code, FieldMaskError.msg_template),
        FieldTypes.digit: (FieldDigitError.code, FieldDigitError.msg_template),
        FieldTypes.invalid: (FieldInvalidError.code, FieldInvalidError.msg_template),
    }

    raise_error(*field_types.get(context))
