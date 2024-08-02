from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNH


class Pessoa(BaseModel):
    cnh: CNH
    nome: str


p1 = Pessoa(nome="João", cnh="18820839790")


print(p1)
# > cnh='18820839790' nome='João'

print(p1.model_dump_json())
# > {"cnh":"18820839790","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cnh': {'example': ['00000000000'],
#                         'format': 'cnh',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cnh',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnh', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
