import re

import pytest
from faker import Faker
from pydantic import BaseModel, ValidationError

from pydantic_br import (
    CNPJ,
    CNPJDigits,
    CNPJMask,
    FieldDigitError,
    FieldInvalidError,
    FieldMaskError,
    FieldTypeError,
)

TOTAL_CNPJ = 10
fake = Faker("pt-BR")


def cnpj_digits():
    cnpjs = [re.sub("[^0-9]", "", fake.cnpj()) for _ in range(TOTAL_CNPJ)]
    return cnpjs


def cnpj_mask():
    cnpjs = [fake.cnpj() for _ in range(TOTAL_CNPJ)]
    return cnpjs


def cnpj_mixed():
    cnpjs = [fake.cnpj() for _ in range(int(TOTAL_CNPJ / 2))]
    cnpjs += [re.sub("[^0-9]", "", fake.cnpj()) for _ in range(int(TOTAL_CNPJ / 2))]
    return cnpjs


@pytest.fixture
def company():
    class Company(BaseModel):
        cnpj: CNPJ

    yield Company


@pytest.fixture
def company_masks():
    class Company(BaseModel):
        cnpj: CNPJMask

    yield Company


@pytest.fixture
def company_digits():
    class Company(BaseModel):
        cnpj: CNPJDigits

    yield Company


@pytest.mark.parametrize("cnpj", cnpj_mixed())
def test_must_be_string(company, cnpj):
    c1 = company(cnpj=cnpj)
    assert isinstance(c1.cnpj, str)


@pytest.mark.parametrize("cnpj", cnpj_mask())
def test_mascara_must_be_string(company_masks, cnpj):
    c1 = company_masks(cnpj=cnpj)
    assert isinstance(c1.cnpj, str)


@pytest.mark.parametrize("cnpj", cnpj_digits())
def test_digits_must_be_string(company_digits, cnpj):
    c1 = company_digits(cnpj=cnpj)
    assert isinstance(c1.cnpj, str)


@pytest.mark.parametrize("cnpj", cnpj_mask())
def test_must_accept_with_mask(company_masks, cnpj):
    c1 = company_masks(cnpj=cnpj)
    assert c1.cnpj == cnpj


@pytest.mark.parametrize("cnpj", cnpj_digits())
def test_must_accept_only_numbers(company_digits, cnpj):
    c1 = company_digits(cnpj=cnpj)
    assert c1.cnpj == cnpj


@pytest.mark.parametrize("cnpj", cnpj_digits())
def test_must_fail_when_use_digits_in_mask_class(company_masks, cnpj):
    with pytest.raises(ValidationError) as e:
        company_masks(cnpj=cnpj)
    assert FieldMaskError.msg_template in str(e.value)


@pytest.mark.parametrize("cnpj", cnpj_mask())
def test_must_fail_when_use_mask_in_digits_class(company_digits, cnpj):
    with pytest.raises(ValidationError) as e:
        company_digits(cnpj=cnpj)
    assert FieldDigitError.msg_template in str(e.value)


@pytest.mark.parametrize("cnpj", cnpj_digits())
def test_must_fail_when_use_another_type(company_digits, cnpj):
    with pytest.raises(ValidationError) as e:
        company_digits(cnpj=int(cnpj))
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("cnpj", cnpj_digits())
def test_must_fail_when_use_invalid_cnpjs(company, cnpj):
    with pytest.raises(ValidationError) as e:
        company(cnpj=cnpj[-1])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cnpj", cnpj_mixed())
def test_must_fail_when_use_digits_cont_above_cnpjs(company, cnpj):
    with pytest.raises(ValidationError) as e:
        company(cnpj=cnpj * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("cnpj", cnpj_mixed())
def test_must_fail_when_use_digits_cont_below_cnpjs(company, cnpj):
    with pytest.raises(ValidationError) as e:
        company(cnpj=cnpj[:5])
    assert FieldInvalidError.msg_template in str(e.value)
