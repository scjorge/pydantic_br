from pydantic import BaseModel

from pydantic_br import Certidao


class Pessoa(BaseModel):
    certidao: Certidao


p1 = Pessoa(certidao="203213.01.55.2019.4.03108.343.1021163-86")
p2 = Pessoa(certidao="20321301552019403108343102116386")

print(p1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86'

print(p1.dict())
# > {'certidao': '203213.01.55.2019.4.03108.343.1021163-86'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}}, 'required': ['certidao']}
print(p2)
# > certidao='20321301552019403108343102116386'

print(p2.dict())
# > {'certidao': '20321301552019403108343102116386'}

print(p2.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}}, 'required': ['certidao']}
