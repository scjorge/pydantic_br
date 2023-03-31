from pydantic import BaseModel

from pydantic_br import CNPJDigits


class Empresa(BaseModel):
    cnpj: CNPJDigits
    cdnpj: CNPJDigits
    nome: str


e1 = Empresa(nome="Empresa 2", cnpj="4280902300019-1", cdnpj="jj")


print(e1)
# > cnpj='42809023000191' nome='Empresa 2'

print(e1.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
