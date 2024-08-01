from pydantic import BaseModel

from pydantic_br import CNS


class Pessoa(BaseModel):
    cns: CNS
    nome: str


p1 = Pessoa(nome="João", cns="162184870250018")

print(p1)
# > cns='162184870250018' nome='João'

print(p1.dict())
# > {'cns': '162184870250018', 'nome': 'João'}

print(p1.schema())
# > {'properties': {'cns': {'format': 'cns', 'title': 'Cns', 'type': 'string'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cns', 'nome'], 'title': 'Pessoa', 'type': 'object'}
