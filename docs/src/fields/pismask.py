from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PISMask


class Pessoa(BaseModel):
    pis: PISMask
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")

print(p1)
# > '848.76001.76-3' nome='João'

print(p1.model_dump_json())
# > {"pis":"848.76001.76-3","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis': {'example': ['000.00000.00-0'],
#                         'format': 'pis mask',
#                         'mask': {'format': 'XXX.XXXXX.XX-X', 'required': True},
#                         'title': 'Pis',
#                         'type': 'string'}},
#  'required': ['pis', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
