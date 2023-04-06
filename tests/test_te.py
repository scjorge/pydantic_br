from string import ascii_letters

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import TE, FieldDigitError, FieldInvalidError, FieldTypeError

te_mock = [
    "867474330655",
    "000880802593",
    "361014230264",
    "301083560680",
    "112130731791",
    "571457320108",
    "028053162186",
    "320412631368",
    "018800821635",
    "234825420418",
]


@pytest.fixture
def person():
    class Person(BaseModel):
        te: TE

    yield Person


@pytest.mark.parametrize("te", te_mock)
def test_must_be_string(person, te):
    p1 = person(te=te)
    assert isinstance(p1.te, str)


@pytest.mark.parametrize("te", te_mock)
def test_must_accept_only_numbers(person, te):
    p1 = person(te=te)
    assert p1.te == te


@pytest.mark.parametrize("te", te_mock)
def test_must_fail_when_use_another_type(person, te):
    with pytest.raises(ValidationError) as e:
        person(te=int(te))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("te", te_mock)
def test_must_fail_when_use_invalid_te(person, te):
    with pytest.raises(ValidationError) as e:
        invalid_te = te[:5] + te[6:]
        person(te=invalid_te)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("te", te_mock)
def test_must_fail_when_use_digits_count_above_te(person, te):
    with pytest.raises(ValidationError) as e:
        person(te=te * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("te", te_mock)
def test_must_fail_when_use_digits_count_below_te(person, te):
    with pytest.raises(ValidationError) as e:
        person(te=te[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "te",
    [
        "000000000000",
        "111111111111",
        "222222222222",
        "333333333333",
        "444444444444",
        "555555555555",
        "666666666666",
        "777777777777",
        "888888888888",
        "999999999999",
    ],
)
def test_must_fail_when_use_sequecial_digits(person, te):
    with pytest.raises(ValidationError) as e:
        person(te=te)
    assert FieldInvalidError.msg_template in str(e.value)


def test_must_fail_when_not_use_only_digits(person):
    with pytest.raises(ValidationError) as e:
        letters = ascii_letters[:11]
        person(te=letters)
    assert FieldDigitError.msg_template in str(e.value)
