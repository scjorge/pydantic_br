from pydantic import BaseModel

from pydantic_br import CNPJDigits, CPFDigits


class Empresa(BaseModel):
    cpf: CPFDigits
    cnpj: CNPJDigits


p = Empresa(nome="Empresa 1", cpf="532.213.947-80", cnpj="42.809.023/0001-91")

"""
p = Empresa(nome="Empresa 1", cpf="532.213.947-80", cnpj="42.809.023/0001-91")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  field only accept digits as string (type=value_error.not_digits)
cnpj
  field only accept digits as string (type=value_error.not_digits)
"""
