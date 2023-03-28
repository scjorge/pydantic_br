import importlib

__all__ = [
    "get_representation",
    "get_pydantic_value_error",
    "get_pydantic_type_error",
]


def _get_pydantic_lib():
    try:
        pydantic_lib = importlib.import_module("pydantic")
    except ModuleNotFoundError:
        raise ValueError("Você instalou o Pydantic antes?")
    return pydantic_lib


def get_representation():
    pydantic_lib = _get_pydantic_lib()
    Representation = pydantic_lib.utils.Representation
    return Representation


def get_pydantic_value_error():
    pydantic_lib = _get_pydantic_lib()
    PydanticValueError = pydantic_lib.PydanticValueError
    return PydanticValueError


def get_pydantic_type_error():
    pydantic_lib = _get_pydantic_lib()
    PydanticTypeError = pydantic_lib.PydanticTypeError
    return PydanticTypeError
