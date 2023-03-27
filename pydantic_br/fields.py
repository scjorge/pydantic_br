from typing import Any, Callable, Dict, Generator

from .utils import get_representation

AnyCallable = Callable[..., Any]
CallableGenerator = Generator[AnyCallable, None, None]
Representation = get_representation()


class CPF:
    __slots__ = ("mask",)

    def __init__(self, mask) -> None:
        self.mask = mask

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type="string", format="cpf")

    def __get_validators__(self) -> CallableGenerator:
        yield self.validate

    def validate(self, value: str) -> str:
        return value
