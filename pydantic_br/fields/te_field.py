from ..validators.te_validator import TEValidator
from .base_field import BaseDigits

__all__ = ["TE"]


class TE(BaseDigits):
    format = "te"
    Validator = TEValidator
    """
    Only Accepts string of TE with digits.

    Attributes:
        number (str): TE number.
    """

    ...
