from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CertidaoMask


class Pessoa(BaseModel):
    certidao: CertidaoMask
    nome: str


p1 = Pessoa(nome="Maria", certidao="203213.01.55.2019.4.03108.343.1021163-86")

print(p1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86' nome='Maria'

print(p1.model_dump_json())
# > {"certidao":"203213.01.55.2019.4.03108.343.1021163-86","nome":"Maria"}

pprint(p1.model_json_schema())
# > {'properties': {'certidao': {'example': ['000000.00.00.0000.0.00000.000.0000000-00'],
#                              'format': 'certidao',
#                              'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                       'required': True},
#                              'title': 'Certidao',
#                              'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['certidao', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
