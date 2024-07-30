from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf: CPF


p = Pessoa(nome="João", cpf="000.000.00-00")

"""
p = Pessoa(nome="João", cpf="000.000.00-00")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Pessoa
cpf
  invalid data (type=value_error.invalid_data)
"""
