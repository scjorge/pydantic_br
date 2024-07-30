from pydantic import BaseModel

from pydantic_br import CertidaoMask


class Pessoa(BaseModel):
    certidao: CertidaoMask
    nome: str


p1 = Pessoa(nome="Maria", certidao="203213.01.55.2019.4.03108.343.1021163-86")

print(p1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86' nome='Maria'

print(p1.dict())
# > {'certidao': '203213.01.55.2019.4.03108.343.1021163-86', 'nome': 'Maria'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['certidao', 'nome']}
