from ..validators.cpf_validator import CPFValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CPF",
    "CPFMask",
    "CPFDigits",
]


class CPF(Base):
    """
    Cadastro de Pessoa Física

    Exemplos: '00000000000' ou '000.000.000-00'
    """

    format = "cpf"
    Validator = CPFValidator
    mask = {"required": False, "format": "000.000.000-00"}
    examples = ["00000000000", "000.000.000-00"]


class CPFMask(BaseMask):
    """
    Cadastro de Pessoa Física

    Exemplos: '000.000.000-00'
    """

    format = "cpf mask"
    Validator = CPFValidator
    mask = {"required": True, "format": "000.000.000-00"}
    examples = ["000.000.000-00"]


class CPFDigits(BaseDigits):
    """
    Cadastro de Pessoa Física

    Exemplos: '00000000000'
    """

    format = "cpf digits"
    Validator = CPFValidator
    examples = ["00000000000"]
