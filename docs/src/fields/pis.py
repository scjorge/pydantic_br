from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PIS


class Pessoa(BaseModel):
    pis1: PIS
    pis2: PIS
    nome: str


p1 = Pessoa(nome="João", pis1="848.76001.76-3", pis2="84876001763")

print(p1)
# > pis='848.76001.76-3' nome='João'

print(p1.model_dump_json())
# > {"pis1":"848.76001.76-3","pis2":"84876001763","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis1': {'example': ['00000000000', '000.00000.00-0'],
#                          'format': 'pis',
#                          'mask': {'format': 'XXX.XXXXX.XX-X',
#                                   'required': False},
#                          'title': 'Pis1',
#                          'type': 'string'},
#                 'pis2': {'example': ['00000000000', '000.00000.00-0'],
#                          'format': 'pis',
#                          'mask': {'format': 'XXX.XXXXX.XX-X',
#                                   'required': False},
#                          'title': 'Pis2',
#                          'type': 'string'}},
#  'required': ['pis1', 'pis2', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
