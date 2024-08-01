from pydantic import BaseModel

from pydantic_br import CNPJMask


class Empresa(BaseModel):
    cnpj: CNPJMask
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.dict())
# > {'cnpj': '42.809.023/0001-91', 'nome': 'Empresa 1'}

print(e1.schema())
# > {'properties': {'cnpj': {'format': 'cnpj', 'title': 'Cnpj', 'type': 'string'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome'], 'title': 'Empresa', 'type': 'object'}
