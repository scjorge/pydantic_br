import re

from .base_validator import FieldValidator

__all__ = ["PlacaVeiculoValidator"]


class PlacaVeiculoValidator(FieldValidator):
    def __init__(self, placa: str) -> None:
        self.placa = placa

    def validate(self) -> bool:
        placa = self.placa
        regex_mercosul = r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$"
        regex_old = r"^[A-Z]{3}[0-9]{4}$"

        if bool(re.match(regex_mercosul, placa)) or bool(re.match(regex_old, placa)):
            return True
        return False
