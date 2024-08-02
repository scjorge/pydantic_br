from pprint import pprint

from pydantic import BaseModel

from pydantic_br import SiglaEstado, CEP


class Endereco(BaseModel):
    cep: CEP
    estado: SiglaEstado


endereco = Endereco(cep="70040010", estado="DF")


print(endereco)
# > cep='70040010' estado='DF'

print(endereco.model_dump_json())
# > {"cep":"70040010","estado":"DF"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep': {'example': ['00000000', '00000-000'],
#                         'format': 'cep',
#                         'mask': {'format': 'XXXXX-XXX', 'required': False},
#                         'title': 'Cep',
#                         'type': 'string'},
#                 'estado': {'example': ['SP', 'DF'],
#                            'format': 'sigla_estado',
#                            'mask': {'format': None, 'required': False},
#                            'title': 'Estado',
#                            'type': 'string'}},
#  'required': ['cep', 'estado'],
#  'title': 'Endereco',
#  'type': 'object'}
