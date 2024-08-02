from ..validators.cep_validator import CEPValidator
from .base_field import Base, BaseDigits, BaseMask

__all__ = [
    "CEP",
    "CEPMask",
    "CEPDigits",
]


class CEP(Base):
    """
    Only Accepts string of CEP.

    Attributes:
        number (str): CEP number.
    """

    format = "cep"
    Validator = CEPValidator
    mask = {"required": False, "format": "XXXXX-XXX"}
    examples = ["00000000", "00000-000"]


class CEPMask(BaseMask):
    """
    Only Accepts string of CEP with mask.

    Attributes:
        number (str): CEP number.
    """

    format = "cep"
    Validator = CEPValidator
    mask = {"required": True, "format": "XXXXX-XXX"}
    examples = ["00000-000"]


class CEPDigits(BaseDigits):
    """
    Only Accepts string of CEP without mask.

    Attributes:
        number (str): CEP number.
    """

    format = "cep"
    Validator = CEPValidator
    mask = {"required": False, "format": None}
    examples = ["00000000"]
