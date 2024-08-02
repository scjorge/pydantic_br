from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf1: CPF
    cpf2: CPF
    nome: str


p1 = Pessoa(nome="João", cpf1="532.213.947-80", cpf2="53221394780")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.model_dump_json())
# > {"cpf1":"532.213.947-80","cpf2":"53221394780","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf1': {'example': ['00000000000', '000.000.000-00'],
#                          'format': 'cpf',
#                          'mask': {'format': '000.000.000-00',
#                                   'required': False},
#                          'title': 'Cpf1',
#                          'type': 'string'},
#                 'cpf2': {'example': ['00000000000', '000.000.000-00'],
#                          'format': 'cpf',
#                          'mask': {'format': '000.000.000-00',
#                                   'required': False},
#                          'title': 'Cpf2',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf1', 'cpf2', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
