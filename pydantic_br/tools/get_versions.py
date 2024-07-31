from enum import Enum

try:
    import pydantic  # noqa
except ModuleNotFoundError:
    raise ModuleNotFoundError("Are you sure you installed Pydantic?")


class PydanticVersion(Enum):
    v1 = 1
    v2 = 2


def get_pydantic_version() -> PydanticVersion:
    if hasattr(pydantic, "__version__"):
        if pydantic.__version__.startswith("1"):
            return PydanticVersion.v1
        if pydantic.__version__.startswith("2"):
            return PydanticVersion.v2
    return PydanticVersion.v1
