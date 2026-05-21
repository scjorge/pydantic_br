import random
import string

from .base_validator import FieldMaskValidator

__all__ = ["CNPJValidator"]


class CNPJValidator(FieldMaskValidator):
    def __init__(self, cnpj) -> None:
        self.cnpj = str(cnpj).upper()
        self.cnpj_alphanumeric = self._get_alphanumeric(cnpj)
        self.weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self.weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def validate_mask(self) -> bool:
        if len(self.cnpj) != 18 or len(self.cnpj_alphanumeric) != 14:
            return False

        return (
            self.cnpj[2:3] == "."
            and self.cnpj[6:7] == "."
            and self.cnpj[10:11] == "/"
            and self.cnpj[15:16] == "-"
        )

    def validate(self) -> bool:
        if len(self.cnpj_alphanumeric) != 14:
            return False

        if any(not c.isalnum() for c in self.cnpj) and not self.validate_mask():
            return False

        first_digit = self._validate_first_digit()
        second_digit = self._validate_second_digit()

        return (
            self.cnpj_alphanumeric[12] == first_digit and self.cnpj_alphanumeric[13] == second_digit
        )

    def generate_cnpj(self, mask: bool = True, alphanumeric: bool = True) -> str:
        def calculate_digit(base: str, weights: list[int]) -> str:
            total = 0

            for i in range(len(weights)):
                total += self._char_value(base[i]) * weights[i]

            remainder = total % 11

            if remainder < 2:
                return "0"

            return str(11 - remainder)

        if alphanumeric:
            chars = string.digits + string.ascii_uppercase
        else:
            chars = string.digits

        base = "".join(random.choice(chars) for _ in range(12))

        dv1 = calculate_digit(base, self.weights1)
        dv2 = calculate_digit(base + dv1, self.weights2)

        cnpj = base + dv1 + dv2

        if not mask:
            return cnpj

        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

    def _char_value(self, c: str) -> int:
        return ord(c) - 48

    def _validate_first_digit(self) -> str:
        total = 0

        for n in range(12):
            value = self._char_value(self.cnpj_alphanumeric[n]) * self.weights1[n]
            total += value

        check_digit = total % 11

        if check_digit < 2:
            first_digit = 0
        else:
            first_digit = 11 - check_digit

        return str(first_digit)

    def _validate_second_digit(self) -> str:
        total = 0

        for n in range(13):
            value = self._char_value(self.cnpj_alphanumeric[n]) * self.weights2[n]
            total += value

        check_digit = total % 11

        if check_digit < 2:
            second_digit = 0
        else:
            second_digit = 11 - check_digit

        return str(second_digit)
