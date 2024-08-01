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
    "134554730167",
    "716263212410",
    "852612232208",
    "164644602518",
    "447572530590",
    "374031350752",
    "616917052089",
    "966488681473",
    "846443231066",
    "757623321180",
    "522824840264",
    "023815261945",
    "116118761880",
    "250269511317",
    "242118621236",
    "682424320833",
    "145851561570",
    "368467080620",
    "074437950302",
    "866381971600",
    "991094882330",
    "197076442607",
    "692662710450",
    "523473200965",
    "061632482119",
    "770155750183",
    "822445242771",
    "826649582801",
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
