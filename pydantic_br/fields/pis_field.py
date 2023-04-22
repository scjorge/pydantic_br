from ..validators.pis_validator import PISValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "PIS",
    "PISMask",
    "PISDigits",
]


class PIS(Base):
    """
    Accepts string of PIS with or without mask.

    Attributes:
        number (str): PIS number.

    """

    format = "pis"
    Validator = PISValidator


class PISMask(BaseMask):
    """
    Only Accepts string of PIS with mask.

    Attributes:
        number (str): PIS number.
    """

    format = "pis mask"
    Validator = PISValidator


class PISDigits(BaseDigits):
    """
    Only Accepts string of PIS with digits.

    Attributes:
        number (str): PIS number.
    """

    format = "pis digits"
    Validator = PISValidator
