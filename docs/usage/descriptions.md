Os tipos de campos disponíveis são extensões para a biblioteca [Pydantic](https://docs.pydantic.dev/).


Todos os campos serão tratados como `string`, mas recebem as validações de cálculos e máscaras.

Os exemplos de dados exemplificados foram tirados dos seguintes sites:


- [geradordecpf](https://www.geradordecpf.org/)
- [4devs](https://www.4devs.com.br/gerador_de_cnpj)

A má utilização dos dados é de total responsabilidade do usuário.

---
## Pessoa Física

CPF

O Cadastro de Pessoa Física é o registro de contribuintes mantido pela Receita Federal do Brasil no qual podem se inscrever, uma única vez, quaisquer pessoas naturais, independentemente de idade ou nacionalidade, inclusive falecidas.

[`CPF`](../field_types/#cpf):

Aceita uma `string` com ou sem máscara. Ex: 61650624409, 605.566.581-67

[`CPFMask`](../field_types/#cpfmask):

Aceita apenas uma `string` de CPF com máscara. Ex: 605.566.581-67

[`CPFDigits`](../field_types/#cpfdigits):

Aceita apenas uma `string` de CPF com digitos. Ex: 61650624409

---

CNH

A Carteira Nacional de Habilitação, também conhecida como carteira de motorista, carta de motorista ou carteira de habilitação é o documento oficial que, no Brasil, atesta a aptidão de um cidadão para conduzir veículos automotores terrestres

[`CNH`](../field_types/#cnh):

Aceita apenas uma `string` com digitos. Ex: 18820839790

---

Título de eleitor

O Título de eleitor é o documento que comprova que um determinado cidadão está inscrito na Justiça Eleitoral do Brasil e se encontra apto a exercer tanto o eleitorado ativo (votar num candidato)

[`TE`](../field_types/#te):

Aceita apenas uma `string` com digitos. Ex: 867474330655

---

PIS

O Programa de Integração Social (PIS) e o Programa de Formação do Patrimônio do Servidor Público (PASEP), mais conhecidos pela sigla PIS/PASEP, são contribuições sociais de natureza tributária, devidas pelas pessoas jurídicas, com objetivo de financiar o pagamento do seguro-desemprego, abono salarial e participação na receita dos órgãos e entidades para os trabalhadores públicos e privados

[`PIS`](../field_types/#pis):

Aceita apenas uma `string` com digitos. Ex: 848.76001.76-3, 84876001763

[`PISMask`](../field_types/#pismask):

Aceita apenas uma `string` com máscara. Ex: 848.76001.76-3

[`PISDigits`](../field_types/#pisdigits):

Aceita apenas uma `string` com digitos. Ex: 84876001763

---

Certidão (Nascimento/Casamento/Óbito)

A certidão de nascimento é um documento cujo conteúdo é extraído do assento de nascimento lavrado em um livro depositado aos cuidados de um cartório de registo civil.

Certidão de casamento é um documento cujo conteúdo é extraído do assento de casamento lavrado em um livro depositado aos cuidados de um cartório de registro civil

Certidão de óbito é um documento cujo conteúdo é extraído do assento de óbito lavrado em um livro depositado aos cuidados de um cartório de Registro Civil.

[`Certidao`](../field_types/#certidao):

Aceita apenas uma `string` com digitos. Ex: 297917.01.55.2022.3.89842.550.6771342-51, 29791701552022389842550677134251

[`CertidaoMask`](../field_types/#certidaomask):

Aceita apenas uma `string` com máscara. Ex: 297917.01.55.2022.3.89842.550.6771342-51

[`CertidaoDigits`](../field_types/#certidaodigits):

Aceita apenas uma `string` com máscara. Ex: 29791701552022389842550677134251

---


CNS

O Cartão Nacional de Saúde - CNS é o documento de identificação do usuário do SUS. Este registro contém as informações dos indivíduos, como: dados pessoais (nome, nome da mãe, data de nascimento, etc), contatos (telefones, endereço, e-mails) e documentos (CPF, RG, Certidões, etc). Atualmente, o número do CNS está inserido nos sistemas informatizados de saúde que demandam a identificação dos indivíduos, sejam usuários, operadores ou profissionais de saúde

[`CNS`](../field_types/#cns):

Aceita apenas uma `string` com digitos. Ex: 873304753530004, 176736924900003

---

## Pessoa Jurídica

CNPJ

O Cadastro Nacional de Pessoas Jurídicas (CNPJ) é o número designado pela Receita Federal na abertura da empresa.

Ele serve para identificar o negócio nos mais diversos tipos de atividades, como a emissão de notas fiscais ou o pagamento dos impostos. 

[`CNPJ`](../field_types/#cnpj):

Aceita uma `string` com ou sem máscara. Ex: 42809023000191, 42.809.023/0001-91


[`CNPJMask`](../field_types/#cnpjmask):

Aceita apenas uma `string` com máscara. Ex: 42.809.023/0001-91


[`CNPJDigits`](../field_types/#cnpjdigits):

Aceita apenas uma `string` com digitos. Ex: 42809023000191

---

## Endereços

CEP

O CEP (Código de Endereçamento Postal) é um conjunto numérico constituído de oito algarismos, que orienta e acelera o encaminhamento, o tratamento e a distribuição de objetos de correspondência, por meio da sua atribuição a localidades, logradouros, unidades dos Correios, serviços, órgãos públicos, empresas e edifícios.

[`CEP`](../field_types/#cep):

Aceita uma `string` com ou sem máscara. Ex: 01310100, 01310-100


[`CEPMask`](../field_types/#cepmask):

Aceita apenas uma `string` com máscara. Ex: 01310-100


[`CEPDigits`](../field_types/#cepdigits):

Aceita apenas uma `string` com digitos. Ex: 01310100


---

Sigla do Estado

Cada uma das 27 unidades federativas do Brasil é representada por uma sigla de duas letras, escrita em letras maiúsculas.

[`SiglaEstado`](../field_types/#siglaestado):

Aceita uma `string` de dois digitos do estado. Ex: AC, DF


---

## Veículos

RENAVAM

O Registro Nacional de Veículos Automotores (RENAVAM) é um sistema desenvolvido pelo Serpro que cobre todo o Brasil, tendo como principal finalidade o registro de todos os veículos do país, efetuados pelas unidades do Detran em cada estado, e centralizados pela unidade central, o Denatran.

[`RENAVAM`](../field_types/#renavam):

Aceita uma `string` com o número do RENAVAM Ex: 97926526793, 62533119251


PlacaVeiculo

Uma placa de identificação (português brasileiro) ou matrícula (português europeu) de veículos é uma chapa de metal ou plástico afixada a um automóvel ou atrelado com o fim da sua identificação oficial. Cada uma destas placas é chamada oficialmente no Brasil placa de identificação de veículos e em Portugal chapa de matrícula de veículos automóveis.

[`PlacaVeiculo`](../field_types/#placaveiculo):

Aceita uma `string`  a Placa do Carro no padrão antigo ou no padrão Mercosul Ex: 97926526793, 62533119251
