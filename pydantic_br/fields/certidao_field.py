from ..validators.certidao_validator import CertidaoValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "Certidao",
    "CertidaoMask",
    "CertidaoDigits",
]


class Certidao(Base):
    """
    Certidão

    Exemplos: '00000000000000000000000000000000' ou '000000.00.00.0000.0.00000.000.0000000-00'
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
    Certidão

    Exemplos: '000000.00.00.0000.0.00000.000.0000000-00'
    """

    format = "certidao"
    Validator = CertidaoValidator
    mask = {"required": True, "format": "XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX"}
    examples = ["000000.00.00.0000.0.00000.000.0000000-00"]


class CertidaoDigits(BaseDigits):
    """
    Certidão

    Exemplos: '00000000000000000000000000000000'
    """

    format = "certidao"
    Validator = CertidaoValidator
    examples = ["00000000000000000000000000000000"]
