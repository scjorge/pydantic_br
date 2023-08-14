from string import ascii_letters

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    Certidao,
    CertidaoDigits,
    FieldDigitError,
    FieldInvalidError,
    FieldTypeError,
)

certidao_mock = [
    "28006901552010301333550237366334",
    "16011901552012304302554893602083",
    "22356301552015348816989150809713",
    "27186901552010396524431903279729",
    "10677301552018365431589899395352",
    "27987501552022352985333151886610",
    "21013801552014317034411432531218",
    "29791701552022389842550677134251",
    "25606201552015310967279760931598",
    "22766101552016375666358876101178",
]


@pytest.fixture
def person():
    class Person(BaseModel):
        certidao: Certidao

    yield Person


@pytest.fixture
def person_only_digits():
    class Person(BaseModel):
        certidao: CertidaoDigits

    yield Person


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_be_string(person, certidao):
    p1 = person(certidao=certidao)
    assert isinstance(p1.certidao, str)


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_accept_only_numbers(person, certidao):
    p1 = person(certidao=certidao)
    assert p1.certidao == certidao


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_fail_when_use_another_type(person, certidao):
    with pytest.raises(ValidationError) as e:
        person(certidao=int(certidao))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_fail_when_use_invalid_certidao(person, certidao):
    with pytest.raises(ValidationError) as e:
        invalid_certidao = certidao[:5] + certidao[6:]
        person(certidao=invalid_certidao)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_fail_when_use_digits_count_above_certidao(person, certidao):
    with pytest.raises(ValidationError) as e:
        person(certidao=certidao * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("certidao", certidao_mock)
def test_must_fail_when_use_digits_count_below_certidao(person, certidao):
    with pytest.raises(ValidationError) as e:
        person(certidao=certidao[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "certidao",
    [
        "00000000000000000000000000000000",
        "11111111111111111111111111111111",
        "22222222222222222222222222222222",
        "33333333333333333333333333333333",
        "44444444444444444444444444444444",
        "55555555555555555555555555555555",
        "66666666666666666666666666666666",
        "77777777777777777777777777777777",
        "88888888888888888888888888888888",
        "99999999999999999999999999999999",
    ],
)
def test_must_fail_when_use_sequecial_digits(person, certidao):
    with pytest.raises(ValidationError) as e:
        person(certidao=certidao)
    assert FieldInvalidError.msg_template in str(e.value)


def test_must_fail_when_not_use_only_digits(person_only_digits):
    with pytest.raises(ValidationError) as e:
        letters = ascii_letters[:32]
        person_only_digits(certidao=letters)
    assert FieldDigitError.msg_template in str(e.value)
