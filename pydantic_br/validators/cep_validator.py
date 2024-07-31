from .base_validator import FieldMaskValidator

__all__ = ["CEPValidator"]


class CEPValidator(FieldMaskValidator):
    def __init__(self, cep) -> None:
        self.cep = cep

    def validate_mask(self) -> bool:
        if len(self.cep) == 9:
            return self.cep[5] == "-"

    def validate(self) -> bool:
        cep = self.cep.replace("-", "")

        if len(cep) != 8:
            return False
        return True
