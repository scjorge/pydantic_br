from typing import TYPE_CHECKING

from .field_erros import *

if TYPE_CHECKING:
    CPF = str
    CNH = str
    CPFMask = str
    CPFDigits = str
    CNPJ = str
    CNPJDigits = str
    CNPJMask = str
    TE = str
    PIS = str
    PISMask = str
    PISDigits = str
    Certidao = str
    CertidaoMask = str
    CertidaoDigits = str
else:
    from .fields.certidao_field import *
    from .fields.cnh_field import *
    from .fields.cnpj_field import *
    from .fields.cpf_field import *
    from .fields.pis_field import *
    from .fields.te_field import *
