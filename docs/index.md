# Pydantic BR

<p align="center">
    <img src="https://raw.githubusercontent.com/scjorge/pydantic_br/master/docs/assets/logo.png" width='200'/>
</p>

<center>
    <p>
        <a href="https://github.com/scjorge/pydantic_br/actions">
            <img src="https://github.com/scjorge/pydantic_br/workflows/CI/badge.svg?event=push"/>
        </a>

        <a href="https://codecov.io/gh/scjorge/pydantic_br">
            <img src="https://codecov.io/gh/scjorge/pydantic_br/branch/master/graph/badge.svg?token=1XVEXSBU69"/>
        </a>

        <a href="https://pypi.org/project/pydantic-br/">
            <img src="https://img.shields.io/pypi/v/pydantic-br"/>
        </a>

        <a href="https://pypi.org/project/pydantic-br/">
            <img src="https://img.shields.io/pypi/pyversions/pydantic-br"/>
        </a>

        <a href="https://github.com/scjorge/pydantic_br/blob/master/LICENSE">
            <img src="https://img.shields.io/pypi/l/pydantic-br"/>
        </a>

        <a href="https://pepy.tech/project/pydantic-br">
            <img src="https://pepy.tech/badge/pydantic-br/month"/>
        </a>
    </p>
</center>

---


Essa é uma biblioteca de extensão e visa disponibilizar campos com validações brasileiras para a biblioteca pydantic.

Compatível com a versão v1 e v2 do Pydantic.



## Disponibilidades

Descrições detalhadas [aqui](usage/descriptions.md).

| Campo | Grupo de Documentos | Nome do Documento | Método de validação
|---|---|---|---|
| CPF | Pessoa física | Cadastro de Pessoa Física | Digito Verificador
| CNH | Pessoa física | Carteira Nacional de Habilitação | Digito Verificador
| TE | Pessoa física  | Título de Eleitor | Digito Verificador
| PIS | Pessoa física  | Programa de Integração Social | Digito Verificador
| CERT | Pessoa física  | Certidão (Nascimento/Casamento/Óbito) | Digito Verificador
| CNS | Pessoa física  | Cartão Nacional de Saúde | Digito Verificador
| CNPJ | Pessoa Jurídica | Carteira Nacional de Pessoas Jurídicas | Digito Verificador
| CEP | Endereços  | Código de Endereçamento Postal | RegExr
| SiglaEstado | Endereços  | Sigla oficial do Estado Brasileiro  | RegExr
| RENAVAM | Veículos | Registro Nacional de Veículos Automotores | Digito Verificador
| PlacaVeiculo | Veículos | Placa do Veículo | RegExr
