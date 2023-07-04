## Pessoa Jurídica


### CNPJ

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

### CNPJMask

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

### CNPJDigits

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

## Pessoa Física
### CPF

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




### CPFMask

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


### CPFDigits

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


### CNH

Aceita o CNH apenas com dígitos

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import CNH


class Pessoa(BaseModel):
    cnh: CNH
    nome: str


p1 = Pessoa(nome="João", cnh="18820839790")


print(p1)
# > cnh='18820839790' nome='João'

print(p1.dict())
# > {'cnh': '18820839790', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'cnh': {'title': 'Cnh', 'type': 'string', 'format': 'cnh'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['cnh', 'nome']}

```

### TE

Aceita o TE apenas com dígitos

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import TE


class Pessoa(BaseModel):
    te: TE
    nome: str


p1 = Pessoa(nome="João", te="867474330655")


print(p1)
# > te='867474330655' nome='João'

print(p1.dict())
# > {'te': '867474330655', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'te': {'title': 'Te', 'type': 'string', 'format': 'te'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['te', 'nome']}
```

### PIS

Aceita o PIS com ou sem máscara

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import PIS


class Pessoa(BaseModel):
    pis: PIS
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")
p2 = Pessoa(nome="Maria", pis="84876001763")

print(p1)
# > pis='848.76001.76-3' nome='João'

print(p1.dict())
# > {'pis': '848.76001.76-3', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}

print(p2)
# > '84876001763' nome='Maria'

print(p2.dict())
# > {'pis': '84876001763', 'nome': 'Maria'}

print(p2.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}

```

### PISMask

Aceita o PIS apenas com máscara

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import PISMask


class Pessoa(BaseModel):
    pis: PISMask
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")

print(p1)
# > '848.76001.76-3' nome='João'

print(p1.dict())
# > {'pis': '848.76001.76-3', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}
```

### PISDigits

Aceita o PIS apenas com dígitos

```{.py3 linenums=1}
from pydantic import BaseModel

from pydantic_br import PISDigits


class Pessoa(BaseModel):
    pis: PISDigits
    nome: str


p1 = Pessoa(nome="João", pis="84876001763")

print(p1)
# > pis='84876001763' nome='João'

print(p1.dict())
# > {'pis': '84876001763', 'nome': 'João'}

print(p1.schema())
# > {'title': 'Pessoa', 'type': 'object', 'properties': {'pis': {'title': 'Pis', 'type': 'string', 'format': 'pis'}, 'nome': {'title': 'Nome', 'type': 'string'}}, 'required': ['pis', 'nome']}
```

### Certidao

Aceita o número da Certidão com ou sem máscara

```{.py3 linenums=1}
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
```

### CertidaoMask

Aceita o número da Certidão apenas com máscara

```{.py3 linenums=1}
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
```

### CertidaoDigits

Aceita o número da Certidão apenas com dígitos

```{.py3 linenums=1}
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
```
