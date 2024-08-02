from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CEP


class Endereco(BaseModel):
    rua: str
    cep1: CEP
    cep2: CEP


endereco = Endereco(rua="Avenida Paulista", cep1="01310100", cep2="01310-100")


print(endereco)
# > rua='Avenida Paulista' cep1='01310100' cep2='01310-100'

print(endereco.model_dump_json())
# > {"rua":"Avenida Paulista","cep1":"01310100","cep2":"01310-100"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep1': {'example': ['00000000', '00000-000'],
#                          'format': 'cep',
#                          'mask': {'format': 'XXXXX-XXX', 'required': False},
#                          'title': 'Cep1',
#                          'type': 'string'},
#                 'cep2': {'example': ['00000000', '00000-000'],
#                          'format': 'cep',
#                          'mask': {'format': 'XXXXX-XXX', 'required': False},
#                          'title': 'Cep2',
#                          'type': 'string'},
#                 'rua': {'title': 'Rua', 'type': 'string'}},
#  'required': ['rua', 'cep1', 'cep2'],
#  'title': 'Endereco',
#  'type': 'object'}
