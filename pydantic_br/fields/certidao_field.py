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


class CertidaoMask(BaseMask):
    """
    Only Accepts string of Certidao with mask.

    Attributes:
        number (str): Certidao number.
    """

    format = "certidao"
    Validator = CertidaoValidator


class CertidaoDigits(BaseDigits):
    """
    Only Accepts string of Certidao with digits.

    Attributes:
        number (str): Certidao number.
    """

    format = "certidao"
    Validator = CertidaoValidator
