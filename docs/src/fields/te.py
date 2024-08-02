from pprint import pprint

from pydantic import BaseModel

from pydantic_br import TE


class Pessoa(BaseModel):
    te: TE
    nome: str


p1 = Pessoa(nome="João", te="867474330655")


print(p1)
# > te='867474330655' nome='João'

print(p1.model_dump_json())
# > {"te":"867474330655","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'te': {'example': ['000000000000'],
#                        'format': 'te',
#                        'mask': {'format': None, 'required': False},
#                        'title': 'Te',
#                        'type': 'string'}},
#  'required': ['te', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
