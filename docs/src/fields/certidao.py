from pydantic import BaseModel

from pydantic_br import Certidao


class Pessoa(BaseModel):
    certidao: Certidao


e1 = Pessoa(certidao="203213.01.55.2019.4.03108.343.1021163-86")
e2 = Pessoa(certidao="20321301552019403108343102116386")

print(e1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86'

print(e1.dict())
# > {'certidao': '203213.01.55.2019.4.03108.343.1021163-86'}

print(e1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}}, 'required': ['certidao']}
print(e2)
# > certidao='20321301552019403108343102116386'

print(e2.dict())
# > {'certidao': '20321301552019403108343102116386'}

print(e2.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'certidao': {'title': 'Certidao', 'type': 'string', 'format': 'certidao'}}, 'required': ['certidao']}
