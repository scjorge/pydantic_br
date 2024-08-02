## Versões do Pydantic 
Os exemplos abaixo estão escritos na versão v1 do Pydantic. Entretanto, funciona perfeitamente com a versão v2.

Então que mudará? Bem, os métodos de 'apresentação' das models foram alterados na v2. 

- O método `dict()` foi alterado para `model_dump()`
- O método `schema()` foi alterado para `model_json_schema()`


## Pessoa Jurídica
### CNPJ

Aceita o CNPJ com ou sem máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJ


class Empresa(BaseModel):
    cnpj1: CNPJ
    cnpj2: CNPJ
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj1="42.809.023/0001-91", cnpj2="42809023000191")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.model_dump_json())
# > {"cnpj1":"42.809.023/0001-91","cnpj2":"42809023000191","nome":"Empresa 1"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj1': {'example': ['00000000000000', '00.000.000/0000-00'],
#                           'format': 'cnpj',
#                           'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                    'required': False},
#                           'title': 'Cnpj1',
#                           'type': 'string'},
#                 'cnpj2': {'example': ['00000000000000', '00.000.000/0000-00'],
#                           'format': 'cnpj',
#                           'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                    'required': False},
#                           'title': 'Cnpj2',
#                           'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj1', 'cnpj2', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
```

### CNPJMask

Aceita o CNPJ apenas com máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJMask


class Empresa(BaseModel):
    cnpj: CNPJMask
    nome: str


e1 = Empresa(nome="Empresa 1", cnpj="42.809.023/0001-91")

print(e1)
# > cnpj='42.809.023/0001-91' nome='Empresa 1'

print(e1.model_dump_json())
# > {"cnpj":"42.809.023/0001-91","nome":"Empresa 1"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj': {'example': ['00.000.000/0000-00'],
#                          'format': 'cnpj',
#                          'mask': {'format': 'XX.XXX.XXX/XXXXX-XX',
#                                   'required': True},
#                          'title': 'Cnpj',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
```

### CNPJDigits

Aceita o CNPJ apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNPJDigits


class Empresa(BaseModel):
    cnpj: CNPJDigits
    nome: str


e1 = Empresa(nome="Empresa 2", cnpj="42809023000191")


print(e1)
# > cnpj='42809023000191' nome='Empresa 2'

print(e1.model_dump_json())
# > {"cnpj":"42809023000191","nome":"Empresa 2"}

pprint(e1.model_json_schema())
# > {'properties': {'cnpj': {'example': ['00000000000000'],
#                          'format': 'cnpj',
#                          'mask': {'format': None, 'required': False},
#                          'title': 'Cnpj',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnpj', 'nome'],
#  'title': 'Empresa',
#  'type': 'object'}
```



## Pessoa Física
### CPF

Aceita o CPF com ou sem máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf1: CPF
    cpf2: CPF
    nome: str


p1 = Pessoa(nome="João", cpf1="532.213.947-80", cpf2="53221394780")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.model_dump_json())
# > {"cpf1":"532.213.947-80","cpf2":"53221394780","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf1': {'example': ['00000000000', '000.000.000-00'],
#                          'format': 'cpf',
#                          'mask': {'format': '000.000.000-00',
#                                   'required': False},
#                          'title': 'Cpf1',
#                          'type': 'string'},
#                 'cpf2': {'example': ['00000000000', '000.000.000-00'],
#                          'format': 'cpf',
#                          'mask': {'format': '000.000.000-00',
#                                   'required': False},
#                          'title': 'Cpf2',
#                          'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf1', 'cpf2', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```




### CPFMask

Aceita o CPF apenas com máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPFMask


class Pessoa(BaseModel):
    cpf: CPFMask
    nome: str


p1 = Pessoa(nome="João", cpf="532.213.947-80")

print(p1)
# > cpf='532.213.947-80' nome='João'

print(p1.model_dump_json())
# > {"cpf":"532.213.947-80","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf': {'example': ['000.000.000-00'],
#                         'format': 'cpf mask',
#                         'mask': {'format': '000.000.000-00', 'required': True},
#                         'title': 'Cpf',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```


### CPFDigits

Aceita o CPF apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPFDigits


class Pessoa(BaseModel):
    cpf: CPFDigits
    nome: str


p1 = Pessoa(nome="João", cpf="53221394780")

print(p1)
# > cpf='53221394780' nome='João'

print(p1.model_dump_json())
# > {"cpf":"53221394780","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cpf': {'example': ['00000000000'],
#                         'format': 'cpf digits',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cpf',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cpf', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```


### CNH

Aceita o CNH apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNH


class Pessoa(BaseModel):
    cnh: CNH
    nome: str


p1 = Pessoa(nome="João", cnh="18820839790")


print(p1)
# > cnh='18820839790' nome='João'

print(p1.model_dump_json())
# > {"cnh":"18820839790","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cnh': {'example': ['00000000000'],
#                         'format': 'cnh',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cnh',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cnh', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### TE

Aceita o TE apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import TE


class Pessoa(BaseModel):
    te: TE
    nome: str


p1 = Pessoa(nome="João", te="867474330655")


print(p1)
# > te='867474330655' nome='João'

print(p1.model_dump_json())
# > {"te":"867474330655","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'te': {'example': ['000000000000'],
#                        'format': 'te',
#                        'mask': {'format': None, 'required': False},
#                        'title': 'Te',
#                        'type': 'string'}},
#  'required': ['te', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### PIS

Aceita o PIS com ou sem máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PIS


class Pessoa(BaseModel):
    pis1: PIS
    pis2: PIS
    nome: str


p1 = Pessoa(nome="João", pis1="848.76001.76-3", pis2="84876001763")

print(p1)
# > pis='848.76001.76-3' nome='João'

print(p1.model_dump_json())
# > {"pis1":"848.76001.76-3","pis2":"84876001763","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis1': {'example': ['00000000000', '000.00000.00-0'],
#                          'format': 'pis',
#                          'mask': {'format': 'XXX.XXXXX.XX-X',
#                                   'required': False},
#                          'title': 'Pis1',
#                          'type': 'string'},
#                 'pis2': {'example': ['00000000000', '000.00000.00-0'],
#                          'format': 'pis',
#                          'mask': {'format': 'XXX.XXXXX.XX-X',
#                                   'required': False},
#                          'title': 'Pis2',
#                          'type': 'string'}},
#  'required': ['pis1', 'pis2', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### PISMask

Aceita o PIS apenas com máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PISMask


class Pessoa(BaseModel):
    pis: PISMask
    nome: str


p1 = Pessoa(nome="João", pis="848.76001.76-3")

print(p1)
# > '848.76001.76-3' nome='João'

print(p1.model_dump_json())
# > {"pis":"848.76001.76-3","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis': {'example': ['000.00000.00-0'],
#                         'format': 'pis mask',
#                         'mask': {'format': 'XXX.XXXXX.XX-X', 'required': True},
#                         'title': 'Pis',
#                         'type': 'string'}},
#  'required': ['pis', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### PISDigits

Aceita o PIS apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PISDigits


class Pessoa(BaseModel):
    pis: PISDigits
    nome: str


p1 = Pessoa(nome="João", pis="84876001763")

print(p1)
# > pis='84876001763' nome='João'

print(p1.model_dump_json())
# > {"pis":"84876001763","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'nome': {'title': 'Nome', 'type': 'string'},
#                 'pis': {'example': ['00000000000'],
#                         'format': 'pis digits',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Pis',
#                         'type': 'string'}},
#  'required': ['pis', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### Certidao

Aceita o número da Certidão com ou sem máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import Certidao


class Pessoa(BaseModel):
    certidao1: Certidao
    certidao2: Certidao


p = Pessoa(
    certidao1="203213.01.55.2019.4.03108.343.1021163-86",
    certidao2="20321301552019403108343102116386",
)


print(p)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86'

print(p.model_dump_json())
# > {"certidao": "203213.01.55.2019.4.03108.343.1021163-86"}

pprint(p.model_json_schema())
# > {'properties': {'certidao1': {'example': ['00000000000000000000000000000000',
#                                           '000000.00.00.0000.0.00000.000.0000000-00'],
#                               'format': 'certidao',
#                               'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                        'required': False},
#                               'title': 'Certidao1',
#                               'type': 'string'},
#                 'certidao2': {'example': ['00000000000000000000000000000000',
#                                           '000000.00.00.0000.0.00000.000.0000000-00'],
#                               'format': 'certidao',
#                               'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                        'required': False},
#                               'title': 'Certidao2',
#                               'type': 'string'}},
#  'required': ['certidao1', 'certidao2'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### CertidaoMask

Aceita o número da Certidão apenas com máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CertidaoMask


class Pessoa(BaseModel):
    certidao: CertidaoMask
    nome: str


p1 = Pessoa(nome="Maria", certidao="203213.01.55.2019.4.03108.343.1021163-86")

print(p1)
# > certidao='203213.01.55.2019.4.03108.343.1021163-86' nome='Maria'

print(p1.model_dump_json())
# > {"certidao":"203213.01.55.2019.4.03108.343.1021163-86","nome":"Maria"}

pprint(p1.model_json_schema())
# > {'properties': {'certidao': {'example': ['000000.00.00.0000.0.00000.000.0000000-00'],
#                              'format': 'certidao',
#                              'mask': {'format': 'XXXXXX.XX.XX.XXXX.X.XXXXX.XXX.XXXXXXX-XX',
#                                       'required': True},
#                              'title': 'Certidao',
#                              'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['certidao', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```

### CertidaoDigits

Aceita o número da Certidão apenas com dígitos

```{.py3 linenums=1}
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
```

### CNS

Aceita o número da CNS apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CNS


class Pessoa(BaseModel):
    cns: CNS
    nome: str


p1 = Pessoa(nome="João", cns="162184870250018")

print(p1)
# > cns='162184870250018' nome='João'

print(p1.model_dump_json())
# > {"cns":"162184870250018","nome":"João"}

pprint(p1.model_json_schema())
# > {'properties': {'cns': {'example': ['000000000000000'],
#                         'format': 'cns',
#                         'mask': {'format': None, 'required': True},
#                         'title': 'Cns',
#                         'type': 'string'},
#                 'nome': {'title': 'Nome', 'type': 'string'}},
#  'required': ['cns', 'nome'],
#  'title': 'Pessoa',
#  'type': 'object'}
```


## Endereços
### CEP

Aceita o CEP com ou sem máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CEP


class Endereco(BaseModel):
    rua: str
    cep1: CEP
    cep2: CEP


endereco = Endereco(rua="Avenida Paulista", cep1="01310100", cep2="01310-100")


print(endereco)
# > rua='Avenida Paulista' cep1='01310100' cep2='01310-100'

print(endereco.model_dump_json())
# > {"rua":"Avenida Paulista","cep1":"01310100","cep2":"01310-100"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep1': {'example': ['00000000', '00000-000'],
#                          'format': 'cep',
#                          'mask': {'format': 'XXXXX-XXX', 'required': False},
#                          'title': 'Cep1',
#                          'type': 'string'},
#                 'cep2': {'example': ['00000000', '00000-000'],
#                          'format': 'cep',
#                          'mask': {'format': 'XXXXX-XXX', 'required': False},
#                          'title': 'Cep2',
#                          'type': 'string'},
#                 'rua': {'title': 'Rua', 'type': 'string'}},
#  'required': ['rua', 'cep1', 'cep2'],
#  'title': 'Endereco',
#  'type': 'object'}
```




### CEPMask

Aceita o CEP apenas com máscara

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CEPMask


class Endereco(BaseModel):
    rua: str
    cep: CEPMask


endereco = Endereco(
    rua="Avenida Paulista",
    cep="01310-100",
)


print(endereco)
# > rua='Avenida Paulista' cep='01310-100'

print(endereco.model_dump_json())
# > {"rua":"Avenida Paulista","cep":"01310-100"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep': {'example': ['00000000'],
#                         'format': 'cep',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cep',
#                         'type': 'string'},
#                 'rua': {'title': 'Rua', 'type': 'string'}},
#  'required': ['rua', 'cep'],
#  'title': 'Endereco',
#  'type': 'object'}
```


### CPFDigits

Aceita o CPF apenas com dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CEPDigits


class Endereco(BaseModel):
    rua: str
    cep: CEPDigits


endereco = Endereco(
    rua="Avenida Paulista",
    cep="01310100",
)


print(endereco)
# > rua='Avenida Paulista' cep='01310100'

print(endereco.model_dump_json())
# > {"rua":"Avenida Paulista","cep":"01310100"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep': {'example': ['00000000'],
#                         'format': 'cep',
#                         'mask': {'format': None, 'required': False},
#                         'title': 'Cep',
#                         'type': 'string'},
#                 'rua': {'title': 'Rua', 'type': 'string'}},
#  'required': ['rua', 'cep'],
#  'title': 'Endereco',
#  'type': 'object'}
```


### SiglaEstado

Aceita a Sigla do estado com dois dígitos

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import SiglaEstado, CEP


class Endereco(BaseModel):
    cep: CEP
    estado: SiglaEstado


endereco = Endereco(cep="70040010", estado="DF")


print(endereco)
# > cep='70040010' estado='DF'

print(endereco.model_dump_json())
# > {"cep":"70040010","estado":"DF"}

pprint(endereco.model_json_schema())
# > {'properties': {'cep': {'example': ['00000000', '00000-000'],
#                         'format': 'cep',
#                         'mask': {'format': 'XXXXX-XXX', 'required': False},
#                         'title': 'Cep',
#                         'type': 'string'},
#                 'estado': {'example': ['SP', 'DF'],
#                            'format': 'sigla_estado',
#                            'mask': {'format': None, 'required': False},
#                            'title': 'Estado',
#                            'type': 'string'}},
#  'required': ['cep', 'estado'],
#  'title': 'Endereco',
#  'type': 'object'}
```


## Veículos
### RENAVAM

Aceita apenas o número do RENAVAM

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import RENAVAM


class Carro(BaseModel):
    ano: str
    renavam: RENAVAM


c1 = Carro(ano="2024", renavam="97926526793")

print(c1)
# > ano='2024' renavam='97926526793'

print(c1.model_dump_json())
# > {"ano":"2024","renavam":"97926526793"}

pprint(c1.model_json_schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'},
#                 'renavam': {'example': ['00000000000'],
#                             'format': 'renavam',
#                             'mask': {'format': None, 'required': False},
#                             'title': 'Renavam',
#                             'type': 'string'}},
#  'required': ['ano', 'renavam'],
#  'title': 'Carro',
#  'type': 'object'}
```

### PlacaVeiculo

Aceita a Placa do Carro no padrão antigo ou no padrão Mercosul.

```{.py3 linenums=1}
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import PlacaVeiculo


class Carro(BaseModel):
    ano: str
    placa: PlacaVeiculo


c1 = Carro(ano="2024", placa="OTM2X22")

print(c1)
# > ano='2024' placa='OTM2X22'

print(c1.model_dump_json())
# > {"ano":"2024","placa":"OTM2X22"}

pprint(c1.model_json_schema())
# > {'properties': {'ano': {'title': 'Ano', 'type': 'string'},
#                 'placa': {'example': ['ABC0000', 'ABC0D00'],
#                           'format': 'placa_veiculo',
#                           'mask': {'format': None, 'required': False},
#                           'title': 'Placa',
#                           'type': 'string'}},
#  'required': ['ano', 'placa'],
#  'title': 'Carro',
#  'type': 'object'}
```
