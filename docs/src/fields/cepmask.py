from pydantic import BaseModel

from pydantic_br import CEPMask


class Endereco(BaseModel):
    rua: str
    cep: CEPMask


endereco = Endereco(
    rua="Avenida Paulista",
    cep="01310-100",
)


print(endereco)
# > rua='Avenida Paulista' cep='01310-100'

print(endereco.model_dump_json())
# > {"rua":"Avenida Paulista","cep":"01310-100"}

print(endereco.model_json_schema())
# > {'properties': {'rua': {'title': 'Rua', 'type': 'string'}, 'cep': {'format': 'cep', 'title': 'Cep', 'type': 'string'}}, 'required': ['rua', 'cep'], 'title': 'Endereco', 'type': 'object'}
