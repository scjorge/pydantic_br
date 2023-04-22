import re
from typing import List

from .base_validator import FieldMaskValidator

__all__ = ["PISValidator"]


class PISValidator(FieldMaskValidator):
    def __init__(self, pis: str) -> None:
        self.pis = pis

    def validate_mask(self) -> bool:
        if len(self.pis) == 14:
            if (
                self.pis[3:4] == "."
                and self.pis[9:10] == "."
                and self.pis[12:13] == "-"
            ):
                return True
        return False

    def validate(self) -> bool:
        pis_numbers = list(re.sub("[^0-9]", "", str(self.pis)))
        pis = [int(n) for n in pis_numbers]

        if len(set(pis)) == 1:
            return False

        if len(pis) != 11:
            return False

        return self._validate_digit(pis)

    def _validate_digit(self, pis: List) -> bool:
        multipliers = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        summation = 0

        for position in range(0, 10):
            summation += int(pis[position]) * multipliers[position]

        module = summation % 11
        dv = 11 - module

        if dv in [10, 11]:
            dv = 0

        return dv == pis[10]
