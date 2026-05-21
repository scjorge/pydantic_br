from .base_validator import FieldMaskValidator

__all__ = ["CPFValidator"]


class CPFValidator(FieldMaskValidator):
    def __init__(self, cpf: str) -> None:
        self.cpf = str(cpf)
        self.cpf_digits = self._get_only_numbers(cpf)

    def validate_mask(self) -> bool:
        if len(self.cpf) != 14 or len(self.cpf_digits) != 11:
            return False

        if self.cpf[3:4] == "." and self.cpf[7:8] == "." and self.cpf[11:12] == "-":
            return True
        return False

    def validate(self) -> bool:
        cpf = self.cpf_digits

        if len(cpf) != 11 or len(set(cpf)) == 1:
            return False

        if any(not c.isdigit() for c in self.cpf) and not self.validate_mask():
            return False

        first_digit = self._validate_first_digit(cpf)
        second_digit = self._validate_second_digit(cpf)
        return cpf[9] == first_digit and cpf[10] == second_digit

    def _validate_first_digit(self, cpf: str) -> str:
        total = 0

        for i in range(10, 1, -1):
            total += int(cpf[10 - i]) * i

        total = (total * 10) % 11

        if total == 10:
            total = 0

        return str(total)

    def _validate_second_digit(self, cpf: str) -> str:
        total = 0

        for i in range(11, 1, -1):
            total += int(cpf[11 - i]) * i

        total = (total * 10) % 11

        if total == 10:
            total = 0

        return str(total)
