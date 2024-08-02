from ..validators.pis_validator import PISValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "PIS",
    "PISMask",
    "PISDigits",
]


class PIS(Base):
    """
    Programa de Integração Social

    Exemplos: '00000000000' ou '000.00000.00-0'
    """

    format = "pis"
    Validator = PISValidator
    mask = {"required": False, "format": "XXX.XXXXX.XX-X"}
    examples = ["00000000000", "000.00000.00-0"]


class PISMask(BaseMask):
    """
    Programa de Integração Social

    Exemplos: '000.00000.00-0'
    """

    format = "pis mask"
    Validator = PISValidator
    mask = {"required": True, "format": "XXX.XXXXX.XX-X"}
    examples = ["000.00000.00-0"]


class PISDigits(BaseDigits):
    """
    Programa de Integração Social

    Exemplos: '00000000000'
    """

    format = "pis digits"
    Validator = PISValidator
    examples = ["00000000000"]
