from pydantic import BaseModel

from pydantic_br import PIS


class Pessoa(BaseModel):
    pis: PIS
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")
p2 = Pessoa(nome="Maria", pis="84876001763")

print(p1)
# > pis='848.76001.76-3' nome='João'

print(p1.dict())
# > {'pis': '848.76001.76-3', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}

print(p2)
# > '84876001763' nome='Maria'

print(p2.dict())
# > {'pis': '84876001763', 'nome': 'Maria'}

print(p2.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}
