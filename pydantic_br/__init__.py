from typing import TYPE_CHECKING

from .field_erros import *

if TYPE_CHECKING:
    CPF = str
    CPFMask = str
    CPFDigits = str
    CNPJ = str
    CNPJDigits = str
    CNPJMask = str
else:
    from .fields.cnpj_field import *
    from .fields.cpf_field import *
