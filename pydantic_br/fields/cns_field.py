from ..validators.cns_validator import CNSValidator
from .base_field import BaseDigits

__all__ = ["CNS"]


class CNS(BaseDigits):
    """
    Only Accepts string of CNS with digits.

    Attributes:
        number (str): CNS number.
    """

    format = "cns"
    Validator = CNSValidator
    mask = {"required": True, "format": None}
    examples = ["000000000000000"]
