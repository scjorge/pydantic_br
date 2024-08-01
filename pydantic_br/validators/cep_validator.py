import re

from .base_validator import FieldMaskValidator

__all__ = ["CEPValidator"]


class CEPValidator(FieldMaskValidator):
    def __init__(self, cep) -> None:
        self.cep = cep

    def validate_mask(self) -> bool:
        if len(re.sub("[^0-9]", "", str(self.cep))) != 8:
            return False

        if len(self.cep) == 9:
            return self.cep[5] == "-"
        return False

    def validate(self) -> bool:
        cep_ranges = [
            ("AC", "69900-000", "69999-999"),
            ("AL", "57000-000", "57999-999"),
            ("AM", "69000-000", "69299-999"),
            ("AM", "69400-000", "69899-999"),
            ("AP", "68900-000", "68999-999"),
            ("BA", "40000-000", "48999-999"),
            ("CE", "60000-000", "63999-999"),
            ("DF", "70000-000", "72799-999"),
            ("DF", "73000-000", "73699-999"),
            ("ES", "29000-000", "29999-999"),
            ("GO", "72800-000", "72999-999"),
            ("GO", "73700-000", "76799-999"),
            ("MA", "65000-000", "65999-999"),
            ("MG", "30000-000", "39999-999"),
            ("MS", "79000-000", "79999-999"),
            ("MT", "78000-000", "78899-999"),
            ("PA", "66000-000", "68899-999"),
            ("PB", "58000-000", "58999-999"),
            ("PE", "50000-000", "56999-999"),
            ("PI", "64000-000", "64999-999"),
            ("PR", "80000-000", "87999-999"),
            ("RJ", "20000-000", "28999-999"),
            ("RN", "59000-000", "59999-999"),
            ("RO", "76800-000", "76999-999"),
            ("RR", "69300-000", "69399-999"),
            ("RS", "90000-000", "99999-999"),
            ("SC", "88000-000", "89999-999"),
            ("SE", "49000-000", "49999-999"),
            ("SP", "01000-000", "19999-999"),
            ("TO", "77000-000", "77999-999"),
        ]

        cep_num = int(self.cep.replace("-", ""))
        for _, start, end in cep_ranges:
            start_num = int(start.replace("-", ""))
            end_num = int(end.replace("-", ""))
            if start_num <= cep_num <= end_num:
                return True
        return False
