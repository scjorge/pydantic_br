from pydantic import BaseModel

from pydantic_br import CPFDigits


class Pessoa(BaseModel):
    cpf: CPFDigits
    nome: str


p1 = Pessoa(nome="João", cpf="53221394780")

print(p1)
# > cpf='53221394780' nome='João'

print(p1.dict())
# > {'cpf': '53221394780', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cpf': {'title': 'Cpf', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cpf', 'nome']}
