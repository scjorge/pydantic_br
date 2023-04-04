Os tipos de campos disponíveis são extensões para a biblioteca [Pydantic](https://docs.pydantic.dev/).


Todos os campos serão tratados como `string`, mas recebem as validações de cálculos e máscaras.

Os exemplos de dados exemplificados foram tirados dos seguintes sites:


- [geradordecpf](https://www.geradordecpf.org/)
- [4devs](https://www.4devs.com.br/gerador_de_cnpj)

A má utilização dos dados é de total responsabilidade do usuário.

---
## Pessoa Física

Para validação do CPF é utilizado o cálculo de digito verificador conforme a [Receita Fereral](https://www.gov.br/receitafederal/pt-br)

[`CPF`](../field_types/#cpf):

Aceita uma `string` CPF com ou sem máscara. Ex: 61650624409, 605.566.581-67


[`CPFMask`](../field_types/#cpfmask):

Aceita apenas uma `string` CPF com máscara. Ex: 605.566.581-67


[`CPFDigits`](../field_types/#cpfdigits):

Aceita apenas uma `string` CPF com digitos. Ex: 61650624409


---

## Pessoa Jurídica

Para validação do CNPJ é utilizado o cálculo de digito verificador conforme o [Gov](https://www.gov.br/receitafederal/pt-br/servicos/cadastro/cnpj)

[`CNPJ`](../field_types/#cnpj):

Aceita uma `string` CNPJ com ou sem máscara. Ex: 42809023000191, 42.809.023/0001-91


[`CNPJMask`](../field_types/#cnpjmask):

Aceita apenas uma `string` CNPJ com máscara. Ex: 42.809.023/0001-91


[`CNPJDigits`](../field_types/#cnpjdigits):

Aceita apenas uma `string` CNPJ com digitos. Ex: 42809023000191