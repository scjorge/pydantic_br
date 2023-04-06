# Pydantic BR

<p align="center">
    <img src="https://raw.githubusercontent.com/scjorge/pydantic_br/master/docs/assets/logo.png" width='200'/>
</p>

<center>

[![CI](https://github.com/scjorge/pydantic_br/workflows/CI/badge.svg?event=push)](https://github.com/scjorge/pydantic_br/actions)
[![codecov](https://codecov.io/gh/scjorge/pydantic_br/branch/master/graph/badge.svg?token=1XVEXSBU69)](https://codecov.io/gh/scjorge/pydantic_br)
[![pypi](https://img.shields.io/pypi/v/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![pypi](https://img.shields.io/pypi/pyversions/pydantic-br)](https://pypi.org/project/pydantic-br/)
[![license](https://img.shields.io/pypi/l/pydantic-br)](https://github.com/scjorge/pydantic_br/blob/master/LICENSE)

</center>

---


Essa é uma biblioteca de extensão e visa disponibilizar campos com validações brasileiras para a biblioteca pydantic.



## Disponibilidades

Descrições detalhadas [aqui](usage/descriptions.md).

| Campo | Grupo de Documentos | Nome do Documento | Método de validação | Situação
|---|---|---|---|---|
| CNPJ | Pessoa Jurídica | Carteira Nacional de Pessoas Jurídicas | Digito Verificador | Concluído
| CPF | Pessoa física | Cadastro de Pessoa Física | Digito Verificador | Concluído
| CNH | Pessoa física | Carteira Nacional de Habilitação | Digito Verificador | Concluído
| TE | Pessoa física  | Título de Eleitor | Digito Verificador | Concluído
| PIS | Pessoa física  | Programa de Integração Social | Digito Verificador | Em desenvolvimento
| CERT | Pessoa física  | Certidão (Nascimento/Casamento/Óbito) | Digito Verificador | Em desenvolvimento
| CNS | Pessoa física  | Cartão Nacional de Saúde | Digito Verificador | Em desenvolvimento
| RNVAM | Veículos | Registro Nacional de Veículos Automotores | RegExr | Em desenvolvimento
| PLACA | Veículos | Placa do Veículo | RegExr | Em desenvolvimento
| ISBN | Livros | Padrão Internacional de Numeração de Livro | Digito Verificador | Em desenvolvimento


