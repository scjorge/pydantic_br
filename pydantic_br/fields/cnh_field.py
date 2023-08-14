from ..validators.cnh_validator import CNHValidator
from .base_field import BaseDigits

__all__ = ["CNH"]


class CNH(BaseDigits):
    """
    Only Accepts string of CNH with digits.

    Attributes:
        number (str): CNH number.
    """

    format = "cnh"
    Validator = CNHValidator
