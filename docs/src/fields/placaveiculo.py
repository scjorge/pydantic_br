from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PlacaVeiculo


class Carro(BaseModel):
    ano: str
    placa: PlacaVeiculo


c1 = Carro(ano="2024", placa="OTM2X22")

print(c1)
# > ano='2024' placa='OTM2X22'

print(c1.model_dump_json())
# > {"ano":"2024","placa":"OTM2X22"}

pprint(c1.model_json_schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'},
#                 'placa': {'example': ['ABC0000', 'ABC0D00'],
#                           'format': 'placa_veiculo',
#                           'mask': {'format': None, 'required': False},
#                           'title': 'Placa',
#                           'type': 'string'}},
#  'required': ['ano', 'placa'],
#  'title': 'Carro',
#  'type': 'object'}
