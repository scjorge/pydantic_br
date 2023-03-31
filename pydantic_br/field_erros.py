from pydantic import PydanticTypeError, PydanticValueError

__all__ = [
    "FieldTypeError",
    "FieldMaskError",
    "FieldDigitError",
    "FieldInvalidError",
]


class FieldTypeError(PydanticTypeError):
    msg_template = "str type expected"


class FieldMaskError(PydanticValueError):
    msg_template = "invalid mask format"


class FieldDigitError(PydanticValueError):
    msg_template = "field only accept digits as string"


class FieldInvalidError(PydanticValueError):
    msg_template = "invalid data"
