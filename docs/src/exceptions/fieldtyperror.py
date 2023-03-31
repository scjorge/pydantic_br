from pydantic import BaseModel

from pydantic_br import CNPJ, CPF


class Empresa(BaseModel):
    cpf: CPF
    cnpj: CNPJ


p = Empresa(nome="Empresa 1", cpf=["532.213.947-80"], cnpj=42809023000191)

"""
p = Empresa(nome="Empresa 1", cpf=["532.213.947-80"], cnpj=42809023000191)
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  str type expected (type=type_error.not_str)
cnpj
  str type expected (type=type_error.not_str)
"""
