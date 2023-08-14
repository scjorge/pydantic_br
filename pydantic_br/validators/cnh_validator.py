import re

from .base_validator import FieldValidator

__all__ = ["CNHValidator"]


class CNHValidator(FieldValidator):
    def __init__(self, cnh: str) -> None:
        self.cnh = cnh

    def validate(self) -> bool:
        cnh = re.sub("[^0-9]", "", str(self.cnh))

        if len(set(cnh)) == 1:
            return False

        if len(cnh) != 11:
            return False

        first_digit = self._validate_first_digit(cnh)
        second_digit = self._validate_second_digit(cnh)
        return cnh[9] == first_digit and cnh[10] == second_digit

    def _validate_first_digit(self, cnh: str) -> str:
        self.dsc = 0
        sum = 0

        for i in range(9, 0, -1):
            sum += int(cnh[9 - i]) * i

        first_digit = sum % 11
        if first_digit >= 10:
            first_digit, self.dsc = 0, 2
        return str(first_digit)

    def _validate_second_digit(self, cnh: str) -> str:
        sum = 0

        for i in range(1, 10):
            sum += int(cnh[i - 1]) * i

        rest = sum % 11

        second_digit = rest - self.dsc
        if second_digit < 0:
            second_digit += 11
        if second_digit >= 10:
            second_digit = 0
        return str(second_digit)
