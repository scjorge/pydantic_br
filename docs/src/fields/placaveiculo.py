from pydantic import BaseModel

from pydantic_br import PlacaVeiculo


class Carro(BaseModel):
    ano: str
    placa: PlacaVeiculo


c1 = Carro(ano="2024", placa="OTM2X22")

print(c1)
# > ano='2024' placa='OTM2X22'

print(c1.dict())
# > {'ano': '2024', 'placa': 'OTM2X22'}

print(c1.schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'}, 'placa': {'format': 'placa_veiculo', 'title': 'Placa', 'type': 'string'}}, 'required': ['ano', 'placa'], 'title': 'Carro', 'type': 'object'}
