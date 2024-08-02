from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJDigits


class Empresa(BaseModel):
    cnpj: CNPJDigits
    nome: str


e1 = Empresa(nome="Empresa 2", cnpj="42809023000191")


print(e1)
# > cnpj='42809023000191' nome='Empresa 2'

print(e1.model_dump_json())
# > {"cnpj":"42809023000191","nome":"Empresa 2"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj': {'example': ['00000000000000'],
#                          'format': 'cnpj',
#                          'mask': {'format': None, 'required': False},
#                          'title': 'Cnpj',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
