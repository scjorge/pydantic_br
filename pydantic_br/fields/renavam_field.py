from ..validators.renavam_validator import RENAVAMValidator
from .base_field import BaseDigits

__all__ = ["RENAVAM"]


class RENAVAM(BaseDigits):
    """
    Only Accepts string of RENAVAM with digits.

    Attributes:
        number (str): RENAVAM number.
    """

    format = "renavam"
    Validator = RENAVAMValidator
