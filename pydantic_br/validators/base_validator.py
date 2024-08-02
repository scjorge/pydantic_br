import re
from abc import ABC, abstractmethod


class FieldValidator(ABC):
    @abstractmethod
    def validate(self):
        ...

    def _get_only_numbers(self, value: str) -> str:
        return re.sub(r"\D", "", value)


class FieldMaskValidator(FieldValidator):
    @abstractmethod
    def validate_mask(self):
        ...
