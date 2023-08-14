from enum import Enum


class PydanticVersion(Enum):
    v1 = 1
    v2 = 2


def get_pydantic_module() -> None:
    try:
        import pydantic  # noqa
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Are you sure you installed Pydantic")


def check_pydantic_v1() -> bool:
    try:
        from pydantic import PydanticTypeError, PydanticValueError  # noqa
    except ImportError:
        return False
    return True


def check_pydantic_v2() -> bool:
    try:
        from pydantic_core import PydanticCustomError  # noqa
    except ImportError:
        return False
    return True


def get_pydantic_version() -> PydanticVersion:
    get_pydantic_module()
    if check_pydantic_v1():
        return PydanticVersion.v1
    if check_pydantic_v2():
        return PydanticVersion.v2
    raise ModuleNotFoundError("Something went wrong withs Pydantic imports")
