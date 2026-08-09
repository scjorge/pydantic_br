from .base_validator import FieldValidator

__all__ = ["SiglaEstadoValidator"]

SIGLAS = frozenset(
    {
        "AC",
        "AL",
        "AM",
        "AP",
        "BA",
        "CE",
        "DF",
        "ES",
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
    }
)


class SiglaEstadoValidator(FieldValidator):
    def __init__(self, sigla: str) -> None:
        self.sigla = str(sigla)

    def validate(self) -> bool:
        if len(self.sigla) != 2 or self.sigla.islower():
            return False
        return self.sigla in SIGLAS
