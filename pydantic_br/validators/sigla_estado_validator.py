from .base_validator import FieldValidator

__all__ = ["SiglaEstadoValidator"]


class SiglaEstadoValidator(FieldValidator):
    def __init__(self, sigla) -> None:
        self.sigla = sigla

    def validate(self) -> bool:
        siglas = [
            "AC",
            "AL",
            "AM",
            "AM",
            "AP",
            "BA",
            "CE",
            "DF",
            "DF",
            "ES",
            "GO",
            "GO",
            "MA",
            "MG",
            "MS",
            "MT",
            "PA",
            "PB",
            "PE",
            "PI",
            "PR",
            "RJ",
            "RN",
            "RO",
            "RR",
            "RS",
            "SC",
            "SE",
            "SP",
            "TO",
        ]
        if len(self.sigla) != 2:
            return False
        return self.sigla in siglas
