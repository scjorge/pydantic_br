from pprint import pprint

from pydantic import BaseModel

from pydantic_br import RENAVAM


class Carro(BaseModel):
    ano: str
    renavam: RENAVAM


c1 = Carro(ano="2024", renavam="97926526793")

print(c1)
# > ano='2024' renavam='97926526793'

print(c1.model_dump_json())
# > {"ano":"2024","renavam":"97926526793"}

pprint(c1.model_json_schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'},
#                 'renavam': {'example': ['00000000000'],
#                             'format': 'renavam',
#                             'mask': {'format': None, 'required': False},
#                             'title': 'Renavam',
#                             'type': 'string'}},
#  'required': ['ano', 'renavam'],
#  'title': 'Carro',
#  'type': 'object'}
