from string import ascii_letters

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import CNH, FieldDigitError, FieldInvalidError, FieldTypeError

cnh_mock = [
    "49761142867",
    "15706519597",
    "18820839790",
    "93025633607",
    "22255370700",
    "74487688509",
    "83002264521",
    "21671642456",
    "36407284795",
    "93017746007",
]


@pytest.fixture
def person():
    class Person(BaseModel):
        cnh: CNH

    yield Person


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_be_string(person, cnh):
    p1 = person(cnh=cnh)
    assert isinstance(p1.cnh, str)


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_accept_only_numbers(person, cnh):
    p1 = person(cnh=cnh)
    assert p1.cnh == cnh


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_fail_when_use_another_type(person, cnh):
    with pytest.raises(ValidationError) as e:
        person(cnh=int(cnh))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_fail_when_use_invalid_cnh(person, cnh):
    with pytest.raises(ValidationError) as e:
        invalid_cnh = cnh[:5] + cnh[6:]
        person(cnh=invalid_cnh)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_fail_when_use_digits_count_above_cnh(person, cnh):
    with pytest.raises(ValidationError) as e:
        person(cnh=cnh * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cnh", cnh_mock)
def test_must_fail_when_use_digits_count_below_cnh(person, cnh):
    with pytest.raises(ValidationError) as e:
        person(cnh=cnh[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "cnh",
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
def test_must_fail_when_use_sequecial_digits(person, cnh):
    with pytest.raises(ValidationError) as e:
        person(cnh=cnh)
    assert FieldInvalidError.msg_template in str(e.value)


def test_must_fail_when_not_use_only_digits(person):
    with pytest.raises(ValidationError) as e:
        letters = ascii_letters[:11]
        person(cnh=letters)
    assert FieldDigitError.msg_template in str(e.value)
