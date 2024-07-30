from pydantic import BaseModel

from pydantic_br import TE


class Pessoa(BaseModel):
    te: TE
    nome: str


p1 = Pessoa(nome="João", te="867474330655")


print(p1)
# > te='867474330655' nome='João'

print(p1.dict())
# > {'te': '867474330655', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'te': {'title': 'Te', 'type': 'string', 'format': 'te'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['te', 'nome']}
