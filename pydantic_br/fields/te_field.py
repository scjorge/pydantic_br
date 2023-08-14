from ..validators.te_validator import TEValidator
from .base_field import BaseDigits

__all__ = ["TE"]


class TE(BaseDigits):
    """
    Only Accepts string of TE with digits.

    Attributes:
        number (str): TE number.
    """

    format = "te"
    Validator = TEValidator
