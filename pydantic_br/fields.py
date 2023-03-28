from typing import Any, Callable, Dict, Generator

from .errors import CPFTypeError, CPFValueError
from .utils import get_representation

__all__ = ["CPF"]

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]
Representation = get_representation()


class CPF(Representation):
    __slots__ = ("mask",)

    def __init__(self, mask: bool = False) -> None:
        self.mask = mask

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format="cpf")

    def __get_validators__(self) -> CallableGenerator:
        yield self.validate_type

    def validate_type(self, value: str) -> str:
        if not isinstance(value, str):
            raise CPFTypeError()
        return value

    def validate_(self, value: str) -> str:
        if not isinstance(value, str):
            raise CPFTypeError()
        return value
