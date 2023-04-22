from abc import ABC, abstractmethod


class FieldValidator(ABC):
    @abstractmethod
    def validate(self):
        ...


class FieldMaskValidator(FieldValidator):
    @abstractmethod
    def validate_mask(self):
        ...
