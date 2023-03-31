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
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}

print(e2)
# > cnpj='42809023000191' nome='Empresa 2'

print(e2.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e2.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
