from ..validators.cep_validator import CEPValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CEP",
    "CEPMask",
    "CEPDigits",
]


class CEP(Base):
    """
    Código de Endereçamento Postal

    Exemplos: '00000000' ou '00000-000'
    """

    format = "cep"
    Validator = CEPValidator
    mask = {"required": False, "format": "XXXXX-XXX"}
    examples = ["00000000", "00000-000"]


class CEPMask(BaseMask):
    """
    Código de Endereçamento Postal

    Exemplos: '00000-000'
    """

    format = "cep"
    Validator = CEPValidator
    mask = {"required": True, "format": "XXXXX-XXX"}
    examples = ["00000-000"]


class CEPDigits(BaseDigits):
    """
    Código de Endereçamento Postal

    Exemplos: '00000000'
    """

    format = "cep"
    Validator = CEPValidator
    examples = ["00000000"]
