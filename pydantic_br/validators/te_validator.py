import re
from typing import List

from .base_validator import FieldValidator

__all__ = ["TEValidator"]


class TEValidator(FieldValidator):
    def __init__(self, te: str) -> None:
        self.te = te
        self.first_check_digit_weights = list(range(2, 10))
        self.second_check_digit_weights = list(range(7, 10))
        self.first_check_digit_doc_slice = slice(0, 8)
        self.second_check_digit_doc_slice = slice(8, 10)

    def validate(self) -> bool:
        te_numbers = list(re.sub("[^0-9]", "", str(self.te)))
        te = [int(n) for n in te_numbers]
        if len(set(te)) == 1:
            return False

        if len(te) != 12:
            return False

        first_check_digit = self._validate_first_digit(te)
        second_check_digit = self._validate_second_digit(
            te=te, first_check_digit=first_check_digit
        )
        return first_check_digit == te[-2] and second_check_digit == te[-1]

    def _validate_first_digit(self, te: List[int]) -> int:
        doc_digits_to_consider = te[self.first_check_digit_doc_slice]
        terms = [
            int(doc_digit * multiplier)
            for doc_digit, multiplier in zip(
                doc_digits_to_consider, self.first_check_digit_weights
            )
        ]

        total = sum(terms)

        if total % 11 == 10:
            return 0

        return total % 11

    def _validate_second_digit(self, te: List[int], first_check_digit: int) -> int:
        doc_digits_to_consider = te[self.second_check_digit_doc_slice] + [
            first_check_digit
        ]
        terms = [
            int(doc_digit * multiplier)
            for doc_digit, multiplier in zip(
                doc_digits_to_consider, self.second_check_digit_weights
            )
        ]

        total = sum(terms)

        if total % 11 == 10:
            return 0

        return total % 11
