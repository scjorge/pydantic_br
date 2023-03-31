## CPF

Aceita o CPF com ou sem máscara

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




## CPFMask

Aceita o CPF apenas com máscara

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CPFMask


class Pessoa(BaseModel):
    cpf: CPFMask
    nome: str


p1 = Pessoa(nome="João", cpf="532.213.947-80")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.dict())
# > {'cpf': '532.213.947-80', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cpf': {'title': 'Cpf', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cpf', 'nome']}
```


## CPFDigits

Aceita o CPF apenas com dígitos

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CPFDigits


class Pessoa(BaseModel):
    cpf: CPFDigits
    nome: str


p1 = Pessoa(nome="João", cpf="53221394780")

print(p1)
# > cpf='53221394780' nome='João'

print(p1.dict())
# > {'cpf': '53221394780', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cpf': {'title': 'Cpf', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cpf', 'nome']}
```

## CNPJ

Aceita o CNPJ com ou sem máscara

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CNPJ


class Empresa(BaseModel):
    cnpj: CNPJ
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")
e2 = Empresa(nome="Empresa 2", cnpj="42809023000191")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.dict())
# > {'cnpj': '42.809.023/0001-91', 'nome': 'Empresa 1'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}

print(e2)
# > cnpj='42809023000191' nome='Empresa 2'

print(e2.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e2.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
```

## CNPJMask

Aceita o CNPJ apenas com máscara

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CNPJMask


class Empresa(BaseModel):
    cnpj: CNPJMask
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.dict())
# > {'cnpj': '42.809.023/0001-91', 'nome': 'Empresa 1'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
```

## CNPJDigits

Aceita o CNPJ apenas com dígitos

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CNPJDigits


class Empresa(BaseModel):
    cnpj: CNPJDigits
    nome: str


e1 = Empresa(nome="Empresa 2", cnpj="42809023000191")


print(e1)
# > cnpj='42809023000191' nome='Empresa 2'

print(e1.dict())
# > {'cnpj': '42809023000191', 'nome': 'Empresa 2'}

print(e1.schema())
# > {'title': 'Empresa', 'type': 'object', 'properties': {'cnpj': {'title': 'Cnpj', 'type': 'string', 'format': 'cpf'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnpj', 'nome']}
```