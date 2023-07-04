from pydantic import BaseModel

from pydantic_br import CertidaoDigits


class Pessoa(BaseModel):
    certidao: CertidaoDigits
    nome: str


p1 = Pessoa(nome="maria", certidao="20321301552019403108343102116386")


print(p1)
# > certidao='20321301552019403108343102116386' nome='maria'

print(p1.dict())
# > {'certidao': '20321301552019403108343102116386', 'nome': 'maria'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['certidao', 'nome']}
