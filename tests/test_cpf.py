import pytest
from pydantic import BaseModel

from pydantic_br import CPF, FieldBR, FieldMaskNumberError


def test_cpf_must_be_string():
    class Pessoa(BaseModel):
        cpf: FieldBR(CPF)

    cpf = "14463381851"
    p1 = Pessoa(cpf=cpf)
    assert isinstance(p1.cpf, str)


def test_cpf_must_accept_with_mask():
    class Pessoa(BaseModel):
        cpf: FieldBR(CPF, force_mask=True)

    cpf = "144.633.818-51"
    p1 = Pessoa(cpf=cpf)
    assert p1.cpf == cpf


def test_cpf_must_accept_only_numbers():
    class Pessoa(BaseModel):
        cpf: FieldBR(CPF, force_numbers=True)

    cpf = "14463381851"
    p1 = Pessoa(cpf=cpf)
    assert p1.cpf == cpf


def test_must_fail_with_force_numbers_and_force_mask_togheter():
    with pytest.raises(FieldMaskNumberError) as exc_info:
        class Pessoa(BaseModel):
            cpf: FieldBR(CPF, force_numbers=True, force_mask=True)

    exception_raised = str(exc_info.value)
    exception_msg = "you can not set force_mask and force_numbers as True togheter"
    assert exception_raised == exception_msg
