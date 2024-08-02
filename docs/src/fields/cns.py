from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNS


class Pessoa(BaseModel):
    cns: CNS
    nome: str


p1 = Pessoa(nome="João", cns="162184870250018")

print(p1)
# > cns='162184870250018' nome='João'

print(p1.model_dump_json())
# > {"cns":"162184870250018","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cns': {'example': ['000000000000000'],
#                         'format': 'cns',
#                         'mask': {'format': None, 'required': True},
#                         'title': 'Cns',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cns', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
