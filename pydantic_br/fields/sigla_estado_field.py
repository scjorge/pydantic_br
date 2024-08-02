from ..validators.sigla_estado_validator import SiglaEstadoValidator
from .base_field import Base

__all__ = ["SiglaEstado"]


class SiglaEstado(Base):
    """
    Only Accepts string of SiglaEstado with digits.

    Attributes:
        number (str): SiglaEstado number.
    """

    format = "sigla_estado"
    Validator = SiglaEstadoValidator
    mask = {"required": False, "format": None}
    examples = ["SP", "DF"]
