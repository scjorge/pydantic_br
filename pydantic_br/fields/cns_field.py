from ..validators.cns_validator import CNSValidator
from .base_field import BaseDigits

__all__ = ["CNS"]


class CNS(BaseDigits):
    """
    Cartão Nacional de Saúde

    Exemplos: '000000000000000'
    """

    format = "cns"
    Validator = CNSValidator
    mask = {"required": True, "format": None}
    examples = ["000000000000000"]
