from .base_validator import FieldMaskValidator

__all__ = ["CertidaoValidator"]


class CertidaoValidator(FieldMaskValidator):
    def __init__(self, certidao) -> None:
        self.certidao = str(certidao)
        self.certidao_digits = self._get_only_numbers(certidao)

    def validate_mask(self) -> bool:
        if len(self.certidao) != 40 or len(self.certidao_digits) != 32:
            return False

        if (
            self.certidao[6:7] == "."
            and self.certidao[9:10] == "."
            and self.certidao[12:13] == "."
            and self.certidao[17:18] == "."
            and self.certidao[19:20] == "."
            and self.certidao[25:26] == "."
            and self.certidao[29:30] == "."
            and self.certidao[37:38] == "-"
        ):
            return True
        return False

    def validate(self) -> bool:
        if len(set(self.certidao_digits)) == 1 or len(self.certidao_digits) != 32:
            return False

        num = list(self.certidao_digits[:-2])
        dv = self.certidao_digits[-2:]

        expected_dv = self._verifying_digit(num)

        return dv == expected_dv

    def _verifying_digit(self, doc: list) -> str:
        dv1 = self._weighted_sum(doc) % 11
        dv1 = 1 if dv1 > 9 else dv1

        dv2 = self._weighted_sum(doc + [dv1]) % 11
        dv2 = 1 if dv2 > 9 else dv2

        return str(dv1) + str(dv2)

    def _weighted_sum(self, value) -> int:
        sum = 0
        multiplier = 32 - len(value)

        for i in range(len(value)):
            sum += int(value[i]) * multiplier

            multiplier += 1
            multiplier = 0 if multiplier > 10 else multiplier

        return sum
