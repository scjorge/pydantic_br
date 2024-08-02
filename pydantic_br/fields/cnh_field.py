from ..validators.cnh_validator import CNHValidator
from .base_field import BaseDigits

__all__ = ["CNH"]


class CNH(BaseDigits):
    """
    Carteira Nacional de Habilitação

    Exemplos: '00000000000'
    """

    format = "cnh"
    Validator = CNHValidator
    examples = ["00000000000"]
