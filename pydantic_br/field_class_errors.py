from typing import Any, Dict, Tuple, Union

from .get_versions import get_pydantic_version

pydantic_version = get_pydantic_version()


class PydanticCustomError(ValueError):
    @property
    def context(self) -> Union[Dict[str, Any], None]:
        ...

    @property
    def type(self) -> str:
        ...

    @property
    def message_template(self) -> str:
        ...

    def message(self) -> str:
        ...


def get_pydantic_errors_class() -> Tuple:
    if pydantic_version.value == 1:
        from pydantic import PydanticTypeError, PydanticValueError
    if pydantic_version.value == 2:

        class PydanticTypeError(PydanticCustomError):  # noqa F811
            ...

        class PydanticValueError(PydanticCustomError):  # noqa F811
            ...

    return PydanticTypeError, PydanticValueError
