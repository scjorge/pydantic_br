from ..validators.cnpj_validator import CNPJValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CNPJ",
    "CNPJMask",
    "CNPJDigits",
]


class CNPJ(Base):
    """
    Accepts string of CNPJ with or without mask.

    Attributes:
        number (str): CNPJ number.

    """

    format = "cnpj"
    Validator = CNPJValidator


class CNPJMask(BaseMask):
    """
    Only Accepts string of CNPJ with mask.

    Attributes:
        number (str): CNPJ number.
    """

    format = "cnpj"
    Validator = CNPJValidator


class CNPJDigits(BaseDigits):
    """
    Only Accepts string of CNPJ with digits.

    Attributes:
        number (str): CNPJ number.
    """

    format = "cnpj"
    Validator = CNPJValidator
