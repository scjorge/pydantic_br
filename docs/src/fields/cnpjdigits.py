from pydantic import BaseModel

from pydantic_br import CNPJDigits


class Empresa(BaseModel):
    cnpj: CNPJDigits
    nome: str


e1 = Empresa(nome="Empresa 2", cnpj="42809023000191")


print(e1)
# > cnpj='42809023000191' nome='Empresa 2'

print(e1.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e1.schema())
# > {'properties': {'cnpj': {'format': 'cnpj', 'title': 'Cnpj', 'type': 'string'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome'], 'title': 'Empresa', 'type': 'object'}
