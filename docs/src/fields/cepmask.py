from pprint import pprint

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

pprint(endereco.model_json_schema())
# > {'properties': {'cep': {'example': ['00000000'],
#                         'format': 'cep',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cep',
#                         'type': 'string'},
#                 'rua': {'title': 'Rua', 'type': 'string'}},
#  'required': ['rua', 'cep'],
#  'title': 'Endereco',
#  'type': 'object'}
