
# Pydantic BR


[![CI](https://github.com/scjorge/pydantic_br/workflows/CI/badge.svg?event=push)](https://github.com/scjorge/pydantic_br/actions)
[![codecov](https://codecov.io/gh/scjorge/pydantic_br/branch/master/graph/badge.svg?token=1XVEXSBU69)](https://codecov.io/gh/scjorge/pydantic_br)
[![pypi](https://img.shields.io/pypi/v/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![pypi](https://img.shields.io/pypi/pyversions/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![license](https://img.shields.io/pypi/l/pydantic-br)](https://github.com/scjorge/pydantic_br/blob/master/LICENSE)


<p align="center">
    <img src="https://raw.githubusercontent.com/scjorge/pydantic_br/master/docs/assets/logo.png" width='200'/>
</p>


Essa é uma biblioteca de extensão e visa disponibilizar campos com validações brasileiras para a biblioteca pydantic.

Compatível com a versão v1 e v2 do Pydantic.


---

Código fonte: https://github.com/scjorge/pydantic_br

Documentação: https://pydantic-br.readthedocs.io

---

## Disponibilidades

| Campo | Grupo de Documentos | Nome do Documento | Método de validação | Situação
|---|---|---|---|---|
| CNPJ | Pessoa Jurídica | Carteira Nacional de Pessoas Jurídicas | Digito Verificador | Concluído
| CPF | Pessoa física | Cadastro de Pessoa Física | Digito Verificador | Concluído
| CNH | Pessoa física | Carteira Nacional de Habilitação | Digito Verificador | Concluído
| TE | Pessoa física  | Título de Eleitor | Digito Verificador | Concluído
| PIS | Pessoa física  | Programa de Integração Social | Digito Verificador | Concluído
| CERT | Pessoa física  | Certidão (Nascimento/Casamento/Óbito) | Digito Verificador | Concluído
| CNS | Pessoa física  | Cartão Nacional de Saúde | Digito Verificador | Em desenvolvimento
| RENAVAM | Veículos | Registro Nacional de Veículos Automotores | RegExr | Em desenvolvimento
| PLACA | Veículos | Placa do Veículo | RegExr | Em desenvolvimento
| ISBN | Livros | Padrão Internacional de Numeração de Livro | Digito Verificador | Em desenvolvimento



## Instalação

### Utilizando pip

```
pip install pydantic-br
```

### Utilizando Poetry

```
poetry add pydantic-br
```

## Exemplos de Utilização

Os exemplos de dados exemplificados foram tirados dos seguintes sites:

- [geradordecpf](https://www.geradordecpf.org/)
- [4devs](https://www.4devs.com.br/gerador_de_cnpj)

A má utilização dos dados é de total responsabilidade do usuário.

### CPF válido 
```python
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPF, CPFDigits, CPFMask


class Pessoa(BaseModel):
    nome: str
    cpf: CPF  # aceita CPF válidos com ou sem máscara
    cpf_mask: CPFMask  # aceita CPF válido apenas com máscara
    cpf_digits: CPFDigits  # aceita CPF válido apnas com dígitos


p1 = Pessoa(
    nome="João", cpf="53221394780", cpf_mask="532.213.947-80", cpf_digits="53221394780"
)


pprint(p1.dict())
```

Saída

```
{'cpf': '53221394780',
 'cpf_digits': '53221394780',
 'cpf_mask': '532.213.947-80',
 'nome': 'João'}
```
### CPF inválido 

```python
from pprint import pprint

from pydantic import BaseModel

from pydantic_br import CPF, CPFDigits, CPFMask


class Pessoa(BaseModel):
    nome: str
    cpf: CPF  # aceita CPF válidos com ou sem máscara
    cpf_mask: CPFMask  # aceita CPF válido apenas com máscara
    cpf_digits: CPFDigits  # aceita CPF válido apenas com dígitos


p1 = Pessoa(
    nome="João", cpf="00000000000", cpf_mask="53221394780", cpf_digits="532.213.947-80"
)

pprint(p1.dict())
```

Saída

```
Traceback (most recent call last):
    p1 = Pessoa(
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 3 validation errors for Pessoa
cpf
  invalid data (type=value_error.invalid_data)
cpf_mask
  invalid mask format (type=value_error.invalid_mask)
cpf_digits
  field only accept digits as string (type=value_error.not_digits)
```

## Versões do Pydantic 
Os exemplos acima estão escritos na versão v1 do Pydantic. Entretanto, funciona perfeitamente com a versão v2.

Então que mudará? Bem, os métodos de 'apresentação' das models foram alterados na v2. 

- O método `dict()` foi alterado para `model_dump()`
- O método `schema()` foi alterado para `model_json_schema()`
