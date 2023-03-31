from pydantic import BaseModel

from pydantic_br import CNPJMask, CPFMask


class Empresa(BaseModel):
    cpf: CPFMask
    cnpj: CNPJMask


p = Empresa(nome="Empresa 1", cpf="53221394780", cnpj="42809023000191")

"""
p = Empresa(nome="Empresa 1", cpf="53221394780", cnpj="42809023000191")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  invalid mask format (type=value_error.invalid_mask)
cnpj
  invalid mask format (type=value_error.invalid_mask)
"""
