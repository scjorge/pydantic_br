from pydantic import BaseModel

from pydantic_br import SiglaEstado, CEP


class Endereco(BaseModel):
    cep: CEP
    estado: SiglaEstado


endereco = Endereco(cep="70040010", estado="DF")


print(endereco)
# > cep='70040010' estado='DF'

print(endereco.dict())
# > {'cep': '70040010', 'estado': 'DF'}

print(endereco.schema())
# > {'properties': {'cep': {'format': 'cep', 'title': 'Cep', 'type': 'string'}, 'estado': {'format': 'sigla_estado', 'title': 'Estado', 'type': 'string'}}, 'required': ['cep', 'estado'], 'title': 'Endereco', 'type': 'object'}
