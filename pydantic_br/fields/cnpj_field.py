from ..validators.cnpj_validator import CNPJValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CNPJ",
    "CNPJMask",
    "CNPJDigits",
]


class CNPJ(Base):
    """
    Cadastro Nacional de Pessoas Jurídicas

    Exemplos: '00000000000000' ou '00.000.000/0000-00'
    """

    format = "cnpj"
    Validator = CNPJValidator
    mask = {"required": False, "format": "XX.XXX.XXX/XXXXX-XX"}
    examples = ["00000000000000", "00.000.000/0000-00"]


class CNPJMask(BaseMask):
    """
    Cadastro Nacional de Pessoas Jurídicas

    Exemplos: '00.000.000/0000-00'
    """

    format = "cnpj"
    Validator = CNPJValidator
    mask = {"required": True, "format": "XX.XXX.XXX/XXXXX-XX"}
    examples = ["00.000.000/0000-00"]


class CNPJDigits(BaseDigits):
    """
    Cadastro Nacional de Pessoas Jurídicas

    Exemplos: '00000000000000'
    """

    format = "cnpj"
    Validator = CNPJValidator
    examples = ["00000000000000"]
