try:
    from pydantic import PydanticTypeError, PydanticValueError
except ModuleNotFoundError:
    raise ModuleNotFoundError("Are you sure you installed pydantic")

__all__ = [
    "FieldTypeError",
    "FieldMaskError",
    "FieldDigitError",
    "FieldInvalidError",
]


class FieldTypeError(PydanticTypeError):
    code = "not_str"
    msg_template = "str type expected"


class FieldMaskError(PydanticValueError):
    code = "invalid_mask"
    msg_template = "invalid mask format"


class FieldDigitError(PydanticValueError):
    code = "not_digits"
    msg_template = "field only accept digits as string"


class FieldInvalidError(PydanticValueError):
    code = "invalid_data"
    msg_template = "invalid data"
