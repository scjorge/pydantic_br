from ..validators.certidao_validator import CertidaoValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "Certidao",
    "CertidaoMask",
    "CertidaoDigits",
]


class Certidao(Base):
    """
    Accepts string of Certidao with or without mask.

    Attributes:
        number (str): Certidao number.
    """

    format = "certidao"
    Validator = CertidaoValidator
    mask = {"required": False, "format": "XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX"}
    examples = [
        "00000000000000000000000000000000",
        "000000.00.00.0000.0.00000.000.0000000-00",
    ]


class CertidaoMask(BaseMask):
    """
    Only Accepts string of Certidao with mask.

    Attributes:
        number (str): Certidao number.
    """

    format = "certidao"
    Validator = CertidaoValidator
    mask = {"required": True, "format": "XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX"}
    examples = ["000000.00.00.0000.0.00000.000.0000000-00"]


class CertidaoDigits(BaseDigits):
    """
    Only Accepts string of Certidao with digits.

    Attributes:
        number (str): Certidao number.
    """

    format = "certidao"
    Validator = CertidaoValidator
    mask = {"required": False, "format": None}
    examples = ["00000000000000000000000000000000"]
