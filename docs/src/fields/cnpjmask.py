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
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
