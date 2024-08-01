from string import ascii_letters

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import CNS, FieldDigitError, FieldInvalidError, FieldTypeError

cns_mock = [
    "162184870250018",
    "176736924900003",
    "960637472190018",
    "184588634730002",
    "873304753530004",
    "209673012590006",
    "263881012570006",
    "759934580130002",
    "249129059110018",
    "147195132580000",
]


@pytest.fixture
def person():
    class Person(BaseModel):
        cns: CNS

    yield Person


@pytest.mark.parametrize("cns", cns_mock)
def test_must_be_string(person, cns):
    p1 = person(cns=cns)
    assert isinstance(p1.cns, str)


@pytest.mark.parametrize("cns", cns_mock)
def test_must_accept_only_numbers(person, cns):
    p1 = person(cns=cns)
    assert p1.cns == cns


@pytest.mark.parametrize("cns", cns_mock)
def test_must_fail_when_use_another_type(person, cns):
    with pytest.raises(ValidationError) as e:
        person(cns=int(cns))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cns", cns_mock)
def test_must_fail_when_use_invalid_cns(person, cns):
    with pytest.raises(ValidationError) as e:
        invalid_cns = cns[0] + cns[:5] + cns[6:]
        person(cns=invalid_cns)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cns", cns_mock)
def test_must_fail_when_use_invalid_cns_fist_digit(person, cns):
    with pytest.raises(ValidationError) as e:
        invalid_cns = cns[1:] + "0"
        person(cns=invalid_cns)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cns", cns_mock)
def test_must_fail_when_use_digits_count_above_cns(person, cns):
    with pytest.raises(ValidationError) as e:
        person(cns=cns * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cns", cns_mock)
def test_must_fail_when_use_digits_count_below_cns(person, cns):
    with pytest.raises(ValidationError) as e:
        person(cns=cns[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "cns",
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
def test_must_fail_when_use_sequecial_digits(person, cns):
    with pytest.raises(ValidationError) as e:
        person(cns=cns)
    assert FieldInvalidError.msg_template in str(e.value)


def test_must_fail_when_not_use_only_digits(person):
    with pytest.raises(ValidationError) as e:
        letters = ascii_letters[:11]
        person(cns=letters)
    assert FieldDigitError.msg_template in str(e.value)
