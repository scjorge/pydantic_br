from typing import Optional
from pydantic import BaseModel, EmailStr, Field

from pydantic_br import CPF, FieldBR


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


def test_cpf_must_remove_mask_with_parameters():
    ...
