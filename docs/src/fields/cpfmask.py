from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPFMask


class Pessoa(BaseModel):
    cpf: CPFMask
    nome: str


p1 = Pessoa(nome="João", cpf="532.213.947-80")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.model_dump_json())
# > {"cpf":"532.213.947-80","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf': {'example': ['000.000.000-00'],
#                         'format': 'cpf mask',
#                         'mask': {'format': '000.000.000-00', 'required': True},
#                         'title': 'Cpf',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
