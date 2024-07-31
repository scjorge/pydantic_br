from pydantic import BaseModel

from pydantic_br import CEP


class Endereco(BaseModel):
    rua: str
    cep: CEP


endereco1 = Endereco(rua="Avenida Paulista", cep="01310100")
endereco2 = Endereco(rua="Avenida Paulista", cep="01310-100")


print(endereco1)
# > rua='Avenida Paulista' cep='01310100'

print(endereco1.model_dump_json())
# > {"rua":"Avenida Paulista","cep":"01310100"}

print(endereco2.model_json_schema())
# > {'properties': {'rua': {'title': 'Rua', 'type': 'string'}, 'cep': {'format': 'cep', 'title': 'Cep', 'type': 'string'}}, 'required': ['rua', 'cep'], 'title': 'Endereco', 'type': 'object'}

print(endereco2)
# > rua='Avenida Paulista' cep='01310-100'

print(endereco2.model_dump_json())
# > {"rua":"Avenida Paulista","cep":"01310-100"}

print(endereco2.model_json_schema())
# > {'properties': {'rua': {'title': 'Rua', 'type': 'string'}, 'cep': {'format': 'cep', 'title': 'Cep', 'type': 'string'}}, 'required': ['rua', 'cep'], 'title': 'Endereco', 'type': 'object'}
