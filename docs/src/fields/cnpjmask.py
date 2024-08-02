from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJMask


class Empresa(BaseModel):
    cnpj: CNPJMask
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.model_dump_json())
# > {"cnpj":"42.809.023/0001-91","nome":"Empresa 1"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj': {'example': ['00.000.000/0000-00'],
#                          'format': 'cnpj',
#                          'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                   'required': True},
#                          'title': 'Cnpj',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
