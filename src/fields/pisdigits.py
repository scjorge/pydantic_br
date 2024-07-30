from pydantic import BaseModel

from pydantic_br import PISDigits


class Pessoa(BaseModel):
    pis: PISDigits
    nome: str


p1 = Pessoa(nome="João", pis="84876001763")

print(p1)
# > pis='84876001763' nome='João'

print(p1.dict())
# > {'pis': '84876001763', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}
