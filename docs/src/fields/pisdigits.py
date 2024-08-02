from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PISDigits


class Pessoa(BaseModel):
    pis: PISDigits
    nome: str


p1 = Pessoa(nome="João", pis="84876001763")

print(p1)
# > pis='84876001763' nome='João'

print(p1.model_dump_json())
# > {"pis":"84876001763","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis': {'example': ['00000000000'],
#                         'format': 'pis digits',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Pis',
#                         'type': 'string'}},
#  'required': ['pis', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
