import re

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    Certidao,
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
    CertidaoDigits,
    CertidaoMask,
)

cert_mock = [
    "280069.01.55.2010.3.01333.550.2373663-34",
    "160119.01.55.2012.3.04302.554.8936020-83",
    "223563.01.55.2015.3.48816.989.1508097-13",
    "271869.01.55.2010.3.96524.431.9032797-29",
    "106773.01.55.2018.3.65431.589.8993953-52",
    "279875.01.55.2022.3.52985.333.1518866-10",
    "210138.01.55.2014.3.17034.411.4325312-18",
    "297917.01.55.2022.3.89842.550.6771342-51",
    "256062.01.55.2015.3.10967.279.7609315-98",
    "227661.01.55.2016.3.75666.358.8761011-78",
]


def cert_digits():
    cert_numbers = [re.sub("[^0-9]", "", str(cert)) for cert in cert_mock]
    return cert_numbers


def cert_mask():
    cert_numbers = cert_mock
    return cert_numbers


def cert_mixed():
    return cert_digits() + cert_mask()


@pytest.fixture
def person():
    class Person(BaseModel):
        cert: Certidao

    yield Person


@pytest.fixture
def person_masks():
    class Person(BaseModel):
        cert: CertidaoMask

    yield Person


@pytest.fixture
def person_digits():
    class Person(BaseModel):
        cert: CertidaoDigits

    yield Person


@pytest.mark.parametrize("cert", cert_mixed())
def test_must_be_string(person, cert):
    p1 = person(cert=cert)
    assert isinstance(p1.cert, str)


@pytest.mark.parametrize("cert", cert_mask())
def test_mask_must_be_string(person_masks, cert):
    p1 = person_masks(cert=cert)
    assert isinstance(p1.cert, str)


@pytest.mark.parametrize("cert", cert_digits())
def test_digits_must_be_string(person_digits, cert):
    p1 = person_digits(cert=cert)
    assert isinstance(p1.cert, str)


@pytest.mark.parametrize("cert", cert_mask())
def test_must_accept_with_mask(person_masks, cert):
    p1 = person_masks(cert=cert)
    assert p1.cert == cert


@pytest.mark.parametrize("cert", cert_digits())
def test_must_accept_only_numbers(person_digits, cert):
    p1 = person_digits(cert=cert)
    assert p1.cert == cert


@pytest.mark.parametrize("cert", cert_digits())
def test_must_fail_when_use_digits_in_mask_class(person_masks, cert):
    with pytest.raises(ValidationError) as e:
        person_masks(cert=cert)
    assert FieldMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("cert", cert_mask())
def test_must_fail_when_use_mask_in_digits_class(person_digits, cert):
    with pytest.raises(ValidationError) as e:
        person_digits(cert=cert)
    assert FieldDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("cert", cert_digits())
def test_must_fail_when_use_another_type(person_digits, cert):
    with pytest.raises(ValidationError) as e:
        person_digits(cert=int(cert))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cert", cert_digits())
def test_must_fail_when_use_invalid_certs(person, cert):
    with pytest.raises(ValidationError) as e:
        person(cert=cert[-1])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cert", cert_mixed())
def test_must_fail_when_use_digits_count_above_certs(person, cert):
    with pytest.raises(ValidationError) as e:
        person(cert=cert * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cert", cert_mixed())
def test_must_fail_when_use_digits_count_below_certs(person, cert):
    with pytest.raises(ValidationError) as e:
        person(cert=cert[:5])
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
        person(cert=certidao)
    assert FieldInvalidError.msg_template in str(e.value)
