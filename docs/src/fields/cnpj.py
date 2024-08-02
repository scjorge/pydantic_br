from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJ


class Empresa(BaseModel):
    cnpj1: CNPJ
    cnpj2: CNPJ
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj1="42.809.023/0001-91", cnpj2="42809023000191")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.model_dump_json())
# > {"cnpj1":"42.809.023/0001-91","cnpj2":"42809023000191","nome":"Empresa 1"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj1': {'example': ['00000000000000', '00.000.000/0000-00'],
#                           'format': 'cnpj',
#                           'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                    'required': False},
#                           'title': 'Cnpj1',
#                           'type': 'string'},
#                 'cnpj2': {'example': ['00000000000000', '00.000.000/0000-00'],
#                           'format': 'cnpj',
#                           'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                    'required': False},
#                           'title': 'Cnpj2',
#                           'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj1', 'cnpj2', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
