from pydantic import BaseModel

from pydantic_br import CertidaoDigits


class Empresa(BaseModel):
    certidao: CertidaoDigits
    nome: str


e1 = Empresa(nome="maria", certidao="20321301552019403108343102116386")


print(e1)
# > certidao='20321301552019403108343102116386' nome='maria'

print(e1.dict())
# > {'certidao': '20321301552019403108343102116386', 'nome': 'maria'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['certidao', 'nome']}
