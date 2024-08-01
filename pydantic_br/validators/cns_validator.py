import re

from .base_validator import FieldValidator

__all__ = ["CNSValidator"]


class CNSValidator(FieldValidator):
    def __init__(self, cns: str) -> None:
        self.cns = cns

    def validate(self) -> bool:
        cns = re.sub("[^0-9]", "", str(self.cns))

        if len(cns) != 15:
            return False

        if len(set(cns)) == 1 or len(cns) == 0:
            return False

        if int(cns[0]) not in [1, 2, 7, 8, 9]:
            return False

        if cns[0] in ["1", "2"]:
            return self._validate_first_case(cns)
        else:
            return self._validate_second_case(cns)

    def _validate_first_case(self, doc: str) -> bool:
        cns = [n for n in doc][:11]
        sum = 0
        for i in range(11):
            sum += int(cns[i]) * (15 - i)

        dv = 11 - (sum % 11)

        if dv == 11:
            dv = 0

        if dv == 10:
            sum += 2
            dv = 11 - (sum % 11)
            cns = cns + ["0", "0", "1", str(dv)]
        else:
            cns = cns + ["0", "0", "0", str(dv)]
        return "".join(cns) == doc

    def _validate_second_case(self, doc: str) -> bool:
        cns = [n for n in doc]
        sum = 0
        for i in range(15):
            sum += int(cns[i]) * (15 - i)
        return sum % 11 == 0
