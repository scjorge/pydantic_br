import re

import pytest
from faker import Faker
from pydantic import BaseModel

from pydantic_br import CPF, CPFDigits, CPFMask

TOTAL_CPF = 10
fake = Faker("pt-BR")


def cpf_digitos():
    cpfs = [re.sub("[^0-9]", "", fake.cpf()) for _ in range(TOTAL_CPF)]
    return cpfs


def cpf_mascaras():
    cpfs = [fake.cpf() for _ in range(TOTAL_CPF)]
    return cpfs


def cpf_misturados():
    cpfs = [fake.cpf() for _ in range(int(TOTAL_CPF / 2))]
    cpfs += [re.sub("[^0-9]", "", fake.cpf()) for _ in range(int(TOTAL_CPF / 2))]
    return cpfs


@pytest.fixture
def pessoa():
    class Pessoa(BaseModel):
        cpf: CPF

    yield Pessoa


@pytest.fixture
def pessoa_com_mascara():
    class Pessoa(BaseModel):
        cpf: CPFMask

    yield Pessoa


@pytest.fixture
def pessoa_somente_digitos():
    class Pessoa(BaseModel):
        cpf: CPFDigits

    yield Pessoa


@pytest.mark.parametrize("cpf", cpf_misturados())
def test_cpf_deve_ser_string(pessoa, cpf):
    p1 = pessoa(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_mascaras())
def test_cpf_mascara_deve_ser_string(pessoa_com_mascara, cpf):
    p1 = pessoa_com_mascara(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_digitos())
def test_cpf_digitos_deve_ser_string(pessoa_somente_digitos, cpf):
    p1 = pessoa_somente_digitos(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_mascaras())
def test_cpf_must_accept_with_mask(pessoa_com_mascara, cpf):
    p1 = pessoa_com_mascara(cpf=cpf)
    assert p1.cpf == cpf


@pytest.mark.parametrize("cpf", cpf_digitos())
def test_cpf_must_accept_only_numbers(pessoa_somente_digitos, cpf):
    p1 = pessoa_somente_digitos(cpf=cpf)
    assert p1.cpf == cpf
