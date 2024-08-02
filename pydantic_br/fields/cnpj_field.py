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
    mask = {"required": False, "format": "XX.XXX.XXX/XXXXX-XX"}
    examples = ["00000000000000", "00.000.000/0000-00"]


class CNPJMask(BaseMask):
    """
    Only Accepts string of CNPJ with mask.

    Attributes:
        number (str): CNPJ number.
    """

    format = "cnpj"
    Validator = CNPJValidator
    mask = {"required": True, "format": "XX.XXX.XXX/XXXXX-XX"}
    examples = ["00.000.000/0000-00"]


class CNPJDigits(BaseDigits):
    """
    Only Accepts string of CNPJ with digits.

    Attributes:
        number (str): CNPJ number.
    """

    format = "cnpj"
    Validator = CNPJValidator
    examples = ["00000000000000"]
