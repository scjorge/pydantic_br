import re

import pytest
from faker import Faker
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    CPF,
    CPFDigitError,
    CPFDigits,
    CPFInvalidError,
    CPFMask,
    CPFMaskError,
    CPFTypeError,
)

TOTAL_CPF = 4
fake = Faker("pt-BR")


def cpf_digits():
    cpfs = [re.sub("[^0-9]", "", fake.cpf()) for _ in range(TOTAL_CPF)]
    return cpfs


def cpf_mask():
    cpfs = [fake.cpf() for _ in range(TOTAL_CPF)]
    return cpfs


def cpf_mixed():
    cpfs = [fake.cpf() for _ in range(int(TOTAL_CPF / 2))]
    cpfs += [re.sub("[^0-9]", "", fake.cpf()) for _ in range(int(TOTAL_CPF / 2))]
    return cpfs


@pytest.fixture
def person():
    class Person(BaseModel):
        cpf: CPF

    yield Person


@pytest.fixture
def person_masks():
    class Person(BaseModel):
        cpf: CPFMask

    yield Person


@pytest.fixture
def person_digits():
    class Person(BaseModel):
        cpf: CPFDigits

    yield Person


@pytest.mark.parametrize("cpf", cpf_mixed())
def test_must_be_string(person, cpf):
    p1 = person(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_mask())
def test_mascara_must_be_string(person_masks, cpf):
    p1 = person_masks(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_digits())
def test_digits_must_be_string(person_digits, cpf):
    p1 = person_digits(cpf=cpf)
    assert isinstance(p1.cpf, str)


@pytest.mark.parametrize("cpf", cpf_mask())
def test_must_accept_with_mask(person_masks, cpf):
    p1 = person_masks(cpf=cpf)
    assert p1.cpf == cpf


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_accept_only_numbers(person_digits, cpf):
    p1 = person_digits(cpf=cpf)
    assert p1.cpf == cpf


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_fail_when_use_mask_in_digits_class(person_masks, cpf):
    with pytest.raises(ValidationError) as e:
        person_masks(cpf=cpf)
    assert CPFMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_mask())
def test_must_fail_when_use_digits_in_mask_class(person_digits, cpf):
    with pytest.raises(ValidationError) as e:
        person_digits(cpf=cpf)
    assert CPFDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_fail_when_use_another_type(person_digits, cpf):
    with pytest.raises(ValidationError) as e:
        person_digits(cpf=int(cpf))
    assert CPFTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_fail_when_use_invalid_cpfs(person, cpf):
    with pytest.raises(ValidationError) as e:
        person(cpf=cpf[-1])
    assert CPFInvalidError.msg_template in str(e.value)
