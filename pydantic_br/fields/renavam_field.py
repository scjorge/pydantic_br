from ..validators.renavam_validator import RENAVAMValidator
from .base_field import BaseDigits

__all__ = ["RENAVAM"]


class RENAVAM(BaseDigits):
    """
    Registro Nacional de Veículos Automotores

    Exemplos: '00000000000'
    """

    format = "renavam"
    Validator = RENAVAMValidator
    examples = ["00000000000"]
