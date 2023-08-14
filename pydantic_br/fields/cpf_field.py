from ..validators.cpf_validator import CPFValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CPF",
    "CPFMask",
    "CPFDigits",
]


class CPF(Base):
    """
    Accepts string of CPF with or without mask.

    Attributes:
        number (str): CPF number.

    """

    format = "cpf"
    Validator = CPFValidator


class CPFMask(BaseMask):
    """
    Only Accepts string of CPF with mask.

    Attributes:
        number (str): CPF number.
    """

    format = "cpf mask"
    Validator = CPFValidator


class CPFDigits(BaseDigits):
    """
    Only Accepts string of CPF with digits.

    Attributes:
        number (str): CPF number.
    """

    format = "cpf digits"
    Validator = CPFValidator
