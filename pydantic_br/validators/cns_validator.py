from .base_validator import FieldValidator

__all__ = ["CNSValidator"]


class CNSValidator(FieldValidator):
    def __init__(self, cns: str) -> None:
        self.cns = cns

    def validate(self) -> bool:
        if int(self.cns[0]) not in [7, 8, 9]:
            return False

        sum = 0
        for i, digit in enumerate(self.cns[:11]):
            sum += int(digit) * (15 - i)

        resto = sum % 11
        verify_digit = 11 - resto if resto != 0 else 0

        return int(self.cns[-4:]) == verify_digit
