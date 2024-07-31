import re

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    CEP,
    CEPDigits,
    CEPMask,
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)

cep_mock = [
    "02202-035",
    "79076-171",
    "21735-590",
    "72410-411",
    "35430-159",
    "35430-159",
    "35430-159",
    "35430-159",
    "35430-159",
    "35430-159",
]


def cep_digits():
    cep_numbers = [re.sub("[^0-9]", "", str(cep)) for cep in cep_mock]
    return cep_numbers


def cep_mask():
    cep_numbers = cep_mock
    return cep_numbers


def cep_mixed():
    return cep_digits() + cep_mask()


@pytest.fixture
def person():
    class Address(BaseModel):
        cep: CEP

    yield Address


@pytest.fixture
def person_masks():
    class Address(BaseModel):
        cep: CEPMask

    yield Address


@pytest.fixture
def person_digits():
    class Address(BaseModel):
        cep: CEPDigits

    yield Address


@pytest.mark.parametrize("cep", cep_mixed())
def test_must_be_string(person, cep):
    p1 = person(cep=cep)
    assert isinstance(p1.cep, str)


@pytest.mark.parametrize("cep", cep_mask())
def test_mascara_must_be_string(person_masks, cep):
    p1 = person_masks(cep=cep)
    assert isinstance(p1.cep, str)


@pytest.mark.parametrize("cep", cep_digits())
def test_digits_must_be_string(person_digits, cep):
    p1 = person_digits(cep=cep)
    assert isinstance(p1.cep, str)


@pytest.mark.parametrize("cep", cep_mask())
def test_must_accept_with_mask(person_masks, cep):
    p1 = person_masks(cep=cep)
    assert p1.cep == cep


@pytest.mark.parametrize("cep", cep_digits())
def test_must_accept_only_numbers(person_digits, cep):
    p1 = person_digits(cep=cep)
    assert p1.cep == cep


@pytest.mark.parametrize("cep", cep_digits())
def test_must_fail_when_use_digits_in_mask_class(person_masks, cep):
    with pytest.raises(ValidationError) as e:
        person_masks(cep=cep)
    assert FieldMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("cep", cep_mask())
def test_must_fail_when_use_mask_in_digits_class(person_digits, cep):
    with pytest.raises(ValidationError) as e:
        person_digits(cep=cep)
    assert FieldDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("cep", cep_digits())
def test_must_fail_when_use_another_type(person_digits, cep):
    with pytest.raises(ValidationError) as e:
        person_digits(cep=int(cep))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cep", cep_digits())
def test_must_fail_when_use_invalid_ceps(person, cep):
    with pytest.raises(ValidationError) as e:
        person(cep=cep[-1])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cep", cep_mixed())
def test_must_fail_when_use_digits_count_above_ceps(person, cep):
    with pytest.raises(ValidationError) as e:
        person(cep=cep * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cep", cep_mixed())
def test_must_fail_when_use_digits_count_below_ceps(person, cep):
    with pytest.raises(ValidationError) as e:
        person(cep=cep[:5])
    assert FieldInvalidError.msg_template in str(e.value)
