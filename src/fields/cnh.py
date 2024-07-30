from pydantic import BaseModel

from pydantic_br import CNH


class Pessoa(BaseModel):
    cnh: CNH
    nome: str


p1 = Pessoa(nome="João", cnh="18820839790")


print(p1)
# > cnh='18820839790' nome='João'

print(p1.dict())
# > {'cnh': '18820839790', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cnh': {'title': 'Cnh', 'type': 'string', 'format': 'cnh'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnh', 'nome']}
