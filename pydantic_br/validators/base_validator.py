import re
from abc import ABC, abstractmethod


class FieldValidator(ABC):
    @abstractmethod
    def validate(self):
        ...

    def _get_only_numbers(self, value: str) -> str:
        return re.sub(r"\D", "", value)

    def _get_alphanumeric(self, value: str) -> str:
        return "".join(filter(str.isalnum, str(value).upper()))

class FieldMaskValidator(FieldValidator):
    @abstractmethod
    def validate_mask(self):
        ...
