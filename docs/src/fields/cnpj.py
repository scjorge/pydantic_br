from pydantic import BaseModel

from pydantic_br import CNPJ


class Empresa(BaseModel):
    cnpj: CNPJ
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")
e2 = Empresa(nome="Empresa 2", cnpj="42809023000191")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.dict())
# > {'cnpj': '42.809.023/0001-91', 'nome': 'Empresa 1'}

print(e1.schema())
# > {'properties': {'cnpj': {'format': 'cnpj', 'title': 'Cnpj', 'type': 'string'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome'], 'title': 'Empresa', 'type': 'object'}

print(e2)
# > cnpj='42809023000191' nome='Empresa 2'

print(e2.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e2.schema())
# > {'properties': {'cnpj': {'format': 'cnpj', 'title': 'Cnpj', 'type': 'string'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome'], 'title': 'Empresa', 'type': 'object'}
