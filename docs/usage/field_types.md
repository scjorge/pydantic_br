Os tipos de campos disponíveis são extensões para a biblioteca [Pydantic](https://docs.pydantic.dev/).


## Descrições
Todos os campos serão tratados como `string`, mas recebem as validações de cálculos e máscaras.

Os exemplos de dados exemplificados foram tirados dos seguintes sites:


- [geradordecpf](https://www.geradordecpf.org/). 
- [4devs](https://www.4devs.com.br/gerador_de_cnpj)


[`CPF`](#cpf):

Aceita uma `string` CPF com ou sem máscara. Ex: 61650624409, 605.566.581-67


[`CPFMask`](#cpfmask):

Aceita apenas uma `string` CPF com máscara. Ex: 605.566.581-67


[`CPFDigits`](#cpfdigits):

Aceita apenas uma `string` CPF com digitos. Ex: 61650624409


---


[`CNPJ`](#cnpj):

Aceita uma `string` CNPJ com ou sem máscara. Ex: 42809023000191, 42.809.023/0001-91


[`CNPJMask`](#cnpjmask):

Aceita apenas uma `string` CNPJ com máscara. Ex: 42.809.023/0001-91


[`CNPJDigits`](#cnpjdigits):

Aceita apenas uma `string` CNPJ com digitos. Ex: 42809023000191



# Campos
## CPF

O campo CPF aceita a string com ou sem máscara. 

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf: CPF
    nome: str


p1 = Pessoa(nome="João", cpf="532.213.947-80")
p2 = Pessoa(nome="Maria", cpf="53221394780")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.dict())
# > {'cpf': '532.213.947-80', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cpf': {'title': 'Cpf', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cpf', 'nome']}

print(p2)
# > cpf='53221394780' nome='Maria'

print(p2.dict())
# > {'cpf': '53221394780', 'nome': 'Maria'}

print(p2.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cpf': {'title': 'Cpf', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cpf', 'nome']}
```