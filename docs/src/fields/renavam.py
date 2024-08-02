from pydantic import BaseModel

from pydantic_br import RENAVAM


class Carro(BaseModel):
    ano: str
    renavam: RENAVAM


c1 = Carro(ano="2024", renavam="97926526793")

print(c1)
# > ano='2024' renavam='97926526793'

print(c1.dict())
# > {'ano': '2024', 'renavam': '97926526793'}

print(c1.schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'}, 'renavam': {'format': 'renavam', 'title': 'Renavam', 'type': 'string'}}, 'required': ['ano', 'renavam'], 'title': 'Carro', 'type': 'object'}
