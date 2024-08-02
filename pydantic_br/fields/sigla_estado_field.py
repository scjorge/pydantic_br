from ..validators.sigla_estado_validator import SiglaEstadoValidator
from .base_field import Base

__all__ = ["SiglaEstado"]


class SiglaEstado(Base):
    """
    Sigla do Estado

    Exemplos: 'SP'
    """

    format = "sigla_estado"
    Validator = SiglaEstadoValidator
    examples = ["SP", "DF"]
