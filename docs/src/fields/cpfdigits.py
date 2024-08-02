from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPFDigits


class Pessoa(BaseModel):
    cpf: CPFDigits
    nome: str


p1 = Pessoa(nome="João", cpf="53221394780")

print(p1)
# > cpf='53221394780' nome='João'

print(p1.model_dump_json())
# > {"cpf":"53221394780","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf': {'example': ['00000000000'],
#                         'format': 'cpf digits',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cpf',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
