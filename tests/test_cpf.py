import re

import pytest
from faker import Faker
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    CPF,
    CPFDigits,
    CPFMask,
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)

TOTAL_CPF = 10
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
def test_must_fail_when_use_digits_in_mask_class(person_masks, cpf):
    with pytest.raises(ValidationError) as e:
        person_masks(cpf=cpf)
    assert FieldMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_mask())
def test_must_fail_when_use_mask_in_digits_class(person_digits, cpf):
    with pytest.raises(ValidationError) as e:
        person_digits(cpf=cpf)
    assert FieldDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_fail_when_use_another_type(person_digits, cpf):
    with pytest.raises(ValidationError) as e:
        person_digits(cpf=int(cpf))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_digits())
def test_must_fail_when_use_invalid_cpfs(person, cpf):
    with pytest.raises(ValidationError) as e:
        person(cpf=cpf[-1])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_mixed())
def test_must_fail_when_use_digits_count_above_cpfs(person, cpf):
    with pytest.raises(ValidationError) as e:
        person(cpf=cpf * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cpf", cpf_mixed())
def test_must_fail_when_use_digits_count_below_cpfs(person, cpf):
    with pytest.raises(ValidationError) as e:
        person(cpf=cpf[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "cpf",
    [
        "00000000000",
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999",
    ],
)
def test_must_fail_when_use_sequecial_digits(person, cpf):
    with pytest.raises(ValidationError) as e:
        person(cpf=cpf)
    assert FieldInvalidError.msg_template in str(e.value)
