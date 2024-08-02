from .base_validator import FieldValidator

__all__ = ["RENAVAMValidator"]


class RENAVAMValidator(FieldValidator):
    def __init__(self, reavam: str) -> None:
        self.renavam = str(reavam)
        self.renavam_digits = self._get_only_numbers(reavam)

    def validate(self) -> bool:
        renavam = self.renavam_digits

        if len(renavam) == 9:
            renavam = "00{}".format(renavam)

        if len(renavam) != 11 or len(set(renavam)) == 1:
            return False

        renavam_with_no_digit = renavam[:-1]
        renavam_with_no_digit = renavam_with_no_digit[::-1]

        sum = 0
        for i, digito in enumerate(renavam_with_no_digit[:8]):
            sum += int(digito) * (i + 2)

        sum += int(renavam_with_no_digit[8]) * 2
        sum += int(renavam_with_no_digit[9]) * 3

        mod11 = sum % 11

        last_computed_number = 11 - mod11

        if last_computed_number >= 10:
            last_computed_number = 0

        return last_computed_number == int(renavam[-1])
