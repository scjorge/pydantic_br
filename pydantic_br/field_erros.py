from .field_class_errors import get_pydantic_errors_class

__all__ = [
    "FieldTypeError",
    "FieldMaskError",
    "FieldDigitError",
    "FieldInvalidError",
]


PydanticTypeError, PydanticValueError = get_pydantic_errors_class()


class FieldTypeError(PydanticTypeError):
    code = "not_str"
    msg_template = "Input should be a valid string"
    message_template = msg_template


class FieldMaskError(PydanticValueError):
    code = "invalid_mask"
    msg_template = "invalid mask format"
    message_template = msg_template


class FieldDigitError(PydanticValueError):
    code = "not_digits"
    msg_template = "field only accept digits as string"
    message_template = msg_template


class FieldInvalidError(PydanticValueError):
    code = "invalid_data"
    msg_template = "invalid data"
    message_template = msg_template
