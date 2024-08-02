import re

from .base_validator import FieldValidator

__all__ = ["RENAVAMValidator"]


class RENAVAMValidator(FieldValidator):
    def __init__(self, reavam: str) -> None:
        self.renavam = reavam

    def validate(self) -> bool:
        renavam = re.sub(r"\D", "", self.renavam)

        if len(renavam) == 9:
            renavam = "00{}".format(renavam)

        if len(renavam) != 11 or len(set(renavam)) == 1:
            return False

        renavam_sem_digito = renavam[:-1]
        renavam_sem_digito = renavam_sem_digito[::-1]

        soma = 0
        for i, digito in enumerate(renavam_sem_digito[:8]):
            soma += int(digito) * (i + 2)

        soma += int(renavam_sem_digito[8]) * 2
        soma += int(renavam_sem_digito[9]) * 3

        mod11 = soma % 11

        ultimo_digito_calculado = 11 - mod11

        if ultimo_digito_calculado >= 10:
            ultimo_digito_calculado = 0

        return ultimo_digito_calculado == int(renavam[-1])
