from pydantic import BaseModel

from pydantic_br import CertidaoMask


class Empresa(BaseModel):
    certidao: CertidaoMask
    nome: str


e1 = Empresa(nome="Maria", certidao="203213.01.55.2019.4.03108.343.1021163-86")

print(e1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86' nome='Maria'

print(e1.dict())
# > {'certidao': '203213.01.55.2019.4.03108.343.1021163-86', 'nome': 'Maria'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['certidao', 'nome']}
