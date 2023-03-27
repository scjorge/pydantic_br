import importlib


def get_representation():
    try:
        utils = importlib.import_module("pydantic.utils")
        Representation = utils.Representation
    except ModuleNotFoundError:
        raise ValueError("Você install o Pydantic antes?")
    return Representation
