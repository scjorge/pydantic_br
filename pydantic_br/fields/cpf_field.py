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
    mask = {"required": False, "format": "000.000.000-00"}
    examples = ["00000000000", "000.000.000-00"]


class CPFMask(BaseMask):
    """
    Only Accepts string of CPF with mask.

    Attributes:
        number (str): CPF number.
    """

    format = "cpf mask"
    Validator = CPFValidator
    mask = {"required": True, "format": "000.000.000-00"}
    examples = ["000.000.000-00"]


class CPFDigits(BaseDigits):
    """
    Only Accepts string of CPF with digits.

    Attributes:
        number (str): CPF number.
    """

    format = "cpf digits"
    Validator = CPFValidator
    mask = {"required": False, "format": None}
    examples = ["00000000000"]
