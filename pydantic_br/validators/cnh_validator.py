from .base_validator import FieldValidator

__all__ = ["CNHValidator"]


class CNHValidator(FieldValidator):
    def __init__(self, cnh: str) -> None:
        self.cnh = str(cnh)
        self.cnh_digits = self._get_only_numbers(cnh)

    def validate(self) -> bool:
        cnh = self.cnh

        if len(self.cnh_digits) != 11 or len(set(self.cnh_digits)) == 1:
            return False

        v = 0
        j = 9

        for i in range(9):
            v += int(cnh[i]) * j
            j -= 1

        dsc = 0
        vl1 = v % 11

        if vl1 >= 10:
            vl1 = 0
            dsc = 2

        v = 0
        j = 1

        for i in range(9):
            v += int(cnh[i]) * j
            j += 1

        x = v % 11
        vl2 = 0 if x >= 10 else x - dsc

        return f"{vl1}{vl2}" == cnh[-2:]
