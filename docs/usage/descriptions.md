Os tipos de campos disponíveis são extensões para a biblioteca [Pydantic](https://docs.pydantic.dev/).


Todos os campos serão tratados como `string`, mas recebem as validações de cálculos e máscaras.

Os exemplos de dados exemplificados foram tirados dos seguintes sites:


- [geradordecpf](https://www.geradordecpf.org/)
- [4devs](https://www.4devs.com.br/gerador_de_cnpj)

A má utilização dos dados é de total responsabilidade do usuário.

---
## Pessoa Física

[`CPF`](../field_types/#cpf):

Aceita uma `string` com ou sem máscara. Ex: 61650624409, 605.566.581-67

[`CPFMask`](../field_types/#cpfmask):

Aceita apenas uma `string` com máscara. Ex: 605.566.581-67

[`CPFDigits`](../field_types/#cpfdigits):

Aceita apenas uma `string` com digitos. Ex: 61650624409

[`CNH`](../field_types/#cnh):

Aceita apenas uma `string` com digitos. Ex: 18820839790

[`TE`](../field_types/#te):

Aceita apenas uma `string` com digitos. Ex: 867474330655

[`PIS`](../field_types/#pis):

Aceita apenas uma `string` com digitos. Ex: 848.76001.76-3, 84876001763

[`PISMask`](../field_types/#pismask):

Aceita apenas uma `string` com máscara. Ex: 848.76001.76-3

[`PISDigits`](../field_types/#pisdigits):

Aceita apenas uma `string` com digitos. Ex: 84876001763

---

## Pessoa Jurídica

[`CNPJ`](../field_types/#cnpj):

Aceita uma `string` com ou sem máscara. Ex: 42809023000191, 42.809.023/0001-91


[`CNPJMask`](../field_types/#cnpjmask):

Aceita apenas uma `string` com máscara. Ex: 42.809.023/0001-91


[`CNPJDigits`](../field_types/#cnpjdigits):

Aceita apenas uma `string` com digitos. Ex: 42809023000191