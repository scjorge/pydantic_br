from typing import Any

__all__ = [
    "FieldTypeError",
    "FieldMaskError",
    "FieldDigitError",
    "FieldInvalidError",
]


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


class FieldTypeError(PydanticTypeError):
    msg_template = "str type expected"


class FieldMaskError(PydanticValueError):
    msg_template = "invalid mask format"


class FieldDigitError(PydanticValueError):
    msg_template = "field only accept digits as string"


class FieldInvalidError(PydanticValueError):
    msg_template = "invalid data"
