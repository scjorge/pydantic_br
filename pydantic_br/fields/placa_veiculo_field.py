from ..validators.placa_veiculo_validator import PlacaVeiculoValidator
from .base_field import Base

__all__ = ["PlacaVeiculo"]


class PlacaVeiculo(Base):
    """
    Accepts string of PlacaVeiculo

    Attributes:
        number (str): PlacaVeiculo number.
    """

    format = "placa_veiculo"
    Validator = PlacaVeiculoValidator
    mask = {"required": False, "format": None}
    examples = ["ABC0000", "ABC0D00"]
