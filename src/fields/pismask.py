from pydantic import BaseModel

from pydantic_br import PISMask


class Pessoa(BaseModel):
    pis: PISMask
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")

print(p1)
# > '848.76001.76-3' nome='João'

print(p1.dict())
# > {'pis': '848.76001.76-3', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}
