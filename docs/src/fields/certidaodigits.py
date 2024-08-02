from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CertidaoDigits


class Pessoa(BaseModel):
    certidao: CertidaoDigits
    nome: str


p1 = Pessoa(nome="maria", certidao="20321301552019403108343102116386")


print(p1)
# > certidao='20321301552019403108343102116386' nome='maria'

print(p1.model_dump_json())
# > {"certidao":"20321301552019403108343102116386","nome":"maria"}

pprint(p1.model_json_schema())
# > {'properties': {'certidao': {'example': ['00000000000000000000000000000000'],
#                              'format': 'certidao',
#                              'mask': {'format': None, 'required': False},
#                              'title': 'Certidao',
#                              'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['certidao', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
