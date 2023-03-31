As classes de validações foram construídas utilizando as classes nativas do pydantic.

- PydanticValueError
- ValidationError

Os detalhes podem ser conferidas [aqui](https://docs.pydantic.dev/usage/models/#error-handling)

---

O pydantic_br utiliza 4 classes para as validações e segue os templetes e cógidos do pydantic.

- FieldTypeError
    - code: "not_str"
    - msg_template: "str type expected"
- FieldMaskError
    - code: "invalid_mask"
    - msg_template: "invalid mask format"
- FieldDigitError
    - code: "not_digits"
    - msg_template: "field only accept digits as string"
- FieldInvalidError
    - code: "invalid_data"
    - msg_template: "invalid data"

---

## FieldTypeError

Essa execeção atende a **todos** os campos disponíveis no pydantic_br. 

Caso tente instanciar um objeto diferente de uma `string`. 

Exemplo:

```python
from pydantic import BaseModel

from pydantic_br import CNPJ, CPF


class Empresa(BaseModel):
    cpf: CPF
    cnpj: CNPJ


p = Empresa(nome="Empresa 1", cpf=["532.213.947-80"], cnpj=42809023000191)
```

```
p = Empresa(nome="Empresa 1", cpf=["532.213.947-80"], cnpj=42809023000191)
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  str type expected (type=type_error.not_str)
cnpj
  str type expected (type=type_error.not_str)
```

---

## FieldMaskError

Essa execeção atende a **todos** os campos disponíveis no pydantic_br que possuem máscara.

Caso tente instanciar um objeto sem a máscara que o campo necessita de acordo com os [detalhes](descriptions.md). O Pydantic levantará uma execeção.

Exemplo:

```python
from pydantic import BaseModel

from pydantic_br import CNPJMask, CPFMask


class Empresa(BaseModel):
    cpf: CPFMask
    cnpj: CNPJMask


p = Empresa(nome="Empresa 1", cpf="53221394780", cnpj="42809023000191")
```

```
p = Empresa(nome="Empresa 1", cpf="53221394780", cnpj="42809023000191")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  invalid mask format (type=value_error.invalid_mask)
cnpj
  invalid mask format (type=value_error.invalid_mask)
```

---

## FieldDigitError

Essa exceção é lenvantada quando um campo que aceita apenas dígitos, recebe máscara.
Caso tente instanciar um objeto com a máscara que o campo necessita de acordo com os [detalhes](descriptions.md). O Pydantic levantará uma execeção.

Exemplo:

```python
from pydantic import BaseModel

from pydantic_br import CPFDigits, CNPJDigits


class Empresa(BaseModel):
    cpf: CPFDigits
    cnpj: CNPJDigits


p = Empresa(nome="Empresa 1", cpf="532.213.947-80", cnpj="42.809.023/0001-91")
```

```
p = Empresa(nome="Empresa 1", cpf="532.213.947-80", cnpj="42.809.023/0001-91")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Empresa
cpf
  field only accept digits as string (type=value_error.not_digits)
cnpj
  field only accept digits as string (type=value_error.not_digits)
```

---

## FieldInvalidError

Essa exceção é lenvantada quando um campo não atende ao requisitos do método utilizado para validação.

Exemplo:

```python
from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf: CPF


p = Pessoa(nome="João", cpf="000.000.00-00")
```

```
p = Pessoa(nome="João", cpf="000.000.00-00")
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Pessoa
cpf
  invalid data (type=value_error.invalid_data)
```