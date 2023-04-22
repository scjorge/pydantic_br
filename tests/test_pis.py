import re

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    PIS,
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
    PISDigits,
    PISMask,
)

pis_mock = [
    "375.98347.21-5",
    "754.35011.66-0",
    "603.48898.33-2",
    "696.42141.52-2",
    "809.84506.52-5",
    "119.75550.32-8",
    "247.85712.30-2",
    "159.99549.72-1",
    "064.19153.59-3",
    "780.39614.96-0",
]


def pis_digits():
    pis_numbers = [re.sub("[^0-9]", "", str(pis)) for pis in pis_mock]
    return pis_numbers


def pis_mask():
    pis_numbers = pis_mock
    return pis_numbers


def pis_mixed():
    return pis_digits() + pis_mask()


@pytest.fixture
def person():
    class Person(BaseModel):
        pis: PIS

    yield Person


@pytest.fixture
def person_masks():
    class Person(BaseModel):
        pis: PISMask

    yield Person


@pytest.fixture
def person_digits():
    class Person(BaseModel):
        pis: PISDigits

    yield Person


@pytest.mark.parametrize("pis", pis_mixed())
def test_must_be_string(person, pis):
    p1 = person(pis=pis)
    assert isinstance(p1.pis, str)


@pytest.mark.parametrize("pis", pis_mask())
def test_mascara_must_be_string(person_masks, pis):
    p1 = person_masks(pis=pis)
    assert isinstance(p1.pis, str)


@pytest.mark.parametrize("pis", pis_digits())
def test_digits_must_be_string(person_digits, pis):
    p1 = person_digits(pis=pis)
    assert isinstance(p1.pis, str)


@pytest.mark.parametrize("pis", pis_mask())
def test_must_accept_with_mask(person_masks, pis):
    p1 = person_masks(pis=pis)
    assert p1.pis == pis


@pytest.mark.parametrize("pis", pis_digits())
def test_must_accept_only_numbers(person_digits, pis):
    p1 = person_digits(pis=pis)
    assert p1.pis == pis


@pytest.mark.parametrize("pis", pis_digits())
def test_must_fail_when_use_digits_in_mask_class(person_masks, pis):
    with pytest.raises(ValidationError) as e:
        person_masks(pis=pis)
    assert FieldMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("pis", pis_mask())
def test_must_fail_when_use_mask_in_digits_class(person_digits, pis):
    with pytest.raises(ValidationError) as e:
        person_digits(pis=pis)
    assert FieldDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("pis", pis_digits())
def test_must_fail_when_use_another_type(person_digits, pis):
    with pytest.raises(ValidationError) as e:
        person_digits(pis=int(pis))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("pis", pis_digits())
def test_must_fail_when_use_invalid_piss(person, pis):
    with pytest.raises(ValidationError) as e:
        person(pis=pis[-1])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("pis", pis_mixed())
def test_must_fail_when_use_digits_count_above_piss(person, pis):
    with pytest.raises(ValidationError) as e:
        person(pis=pis * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("pis", pis_mixed())
def test_must_fail_when_use_digits_count_below_piss(person, pis):
    with pytest.raises(ValidationError) as e:
        person(pis=pis[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "pis",
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
def test_must_fail_when_use_sequecial_digits(person, pis):
    with pytest.raises(ValidationError) as e:
        person(pis=pis)
    assert FieldInvalidError.msg_template in str(e.value)
