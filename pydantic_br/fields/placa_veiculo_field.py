from ..validators.placa_veiculo_validator import PlacaVeiculoValidator
from .base_field import Base

__all__ = ["PlacaVeiculo"]


class PlacaVeiculo(Base):
    """
    Placa veicular

    Exemplos: 'ABC0000' ou 'ABC0D00'
    """

    format = "placa_veiculo"
    Validator = PlacaVeiculoValidator
    examples = ["ABC0000", "ABC0D00"]
