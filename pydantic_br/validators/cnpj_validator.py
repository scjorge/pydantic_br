from .base_validator import FieldMaskValidator

__all__ = ["CNPJValidator"]


class CNPJValidator(FieldMaskValidator):
    def __init__(self, cnpj) -> None:
        self.cnpj = str(cnpj)
        self.cnpj_digits = self._get_only_numbers(cnpj)

    def validate_mask(self) -> bool:
        if len(self.cnpj) != 18 or len(self.cnpj_digits) != 14:
            return False

        if (
            self.cnpj[2:3] == "."
            and self.cnpj[6:7] == "."
            and self.cnpj[10:11] == "/"
            and self.cnpj[15:16] == "-"
        ):
            return True
        return False

    def validate(self) -> bool:
        if len(self.cnpj_digits) != 14:
            return False

        first_digit = self._validate_first_digit()
        second_digit = self._validate_second_digit()
        return (
            self.cnpj_digits[12] == first_digit and self.cnpj_digits[13] == second_digit
        )

    def _validate_first_digit(self) -> str:
        sum = 0
        weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        for n in range(12):
            value = int(self.cnpj_digits[n]) * weight[n]
            sum = sum + value

        check_digit = sum % 11

        if check_digit < 2:
            first_digit = 0
        else:
            first_digit = 11 - check_digit
        return str(first_digit)

    def _validate_second_digit(self) -> str:
        sum = 0
        weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for n in range(13):
            sum = sum + int(self.cnpj_digits[n]) * weight[n]

        check_digit = sum % 11

        if check_digit < 2:
            second_digit = 0
        else:
            second_digit = 11 - check_digit
        return str(second_digit)
