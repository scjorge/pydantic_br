from ..validators.te_validator import TEValidator
from .base_field import BaseDigits

__all__ = ["TE"]


class TE(BaseDigits):
    """
    Título Eleitoral

    Exemplos: '000000000000'
    """

    format = "te"
    Validator = TEValidator
    examples = ["000000000000"]
