Os tipos de campos disponíveis são extensões da biblioteca [Pydantic](https://docs.pydantic.dev/). Por tanto cada campo é um objeto nativo do tipo Pydantic.

## Descrição
*pydantic_br* possui campos brasileiros de validação. Todos os campos são tratatos como `string`, mas recebem as validações de cálculos e máscaras

`CPF`: Campo segue os cálculos da [receita federal](https://www.gov.br/receitafederal/pt-br).


## CPF

Por padrão o campo CPF aceita a string com ou sem máscara. 

```python
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