from string import ascii_letters

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import FieldDigitError, FieldInvalidError, FieldTypeError, RENAVAM

renavam_mock = [
    "98514973286",
    "12773225700",
    "12367742369",
    "56157886129",
    "27757318462",
    "74486587103",
    "00520934156",
    "89567842861",
    "13873311762",
    "11019417514",
]


@pytest.fixture
def car():
    class Car(BaseModel):
        renavam: RENAVAM

    yield Car


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_be_string(car, renavam):
    p1 = car(renavam=renavam)
    assert isinstance(p1.renavam, str)


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_accept_only_numbers(car, renavam):
    p1 = car(renavam=renavam)
    assert p1.renavam == renavam


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_fail_when_use_another_type(car, renavam):
    with pytest.raises(ValidationError) as e:
        car(renavam=int(renavam))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_fail_when_use_invalid_renavam(car, renavam):
    with pytest.raises(ValidationError) as e:
        invalid_renavam = renavam[0] + renavam[:5] + renavam[6:]
        car(renavam=invalid_renavam)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_fail_when_use_digits_count_above_renavam(car, renavam):
    with pytest.raises(ValidationError) as e:
        car(renavam=renavam * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("renavam", renavam_mock)
def test_must_fail_when_use_digits_count_below_renavam(car, renavam):
    with pytest.raises(ValidationError) as e:
        car(renavam=renavam[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "renavam",
    [
        "000000000000000",
        "111111111111111",
        "222222222222222",
        "333333333333333",
        "444444444444444",
        "555555555555555",
        "666666666666666",
        "777777777777777",
        "888888888888888",
        "999999999999999",
    ],
)
def test_must_fail_when_use_sequecial_digits(car, renavam):
    with pytest.raises(ValidationError) as e:
        car(renavam=renavam)
    assert FieldInvalidError.msg_template in str(e.value)


def test_must_fail_when_not_use_only_digits(car):
    with pytest.raises(ValidationError) as e:
        letters = ascii_letters[:11]
        car(renavam=letters)
    assert FieldDigitError.msg_template in str(e.value)
