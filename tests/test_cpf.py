from pydantic import BaseModel

from pydantic_br import CPF


def test_cpf_must_be_string():
    class Pessoa(BaseModel):
        cpf: CPF

    cpf = "14463381851"
    p1 = Pessoa(cpf=cpf)
    assert isinstance(p1.cpf, str)


def test_cpf_must_accept_with_mask():
    class Pessoa(BaseModel):
        cpf: CPF

    cpf = "144.633.818-51"
    p1 = Pessoa(cpf=cpf)
    assert p1.cpf == cpf


def test_cpf_must_accept_only_numbers():
    class Pessoa(BaseModel):
        cpf: CPF

    cpf = "14463381851"
    p1 = Pessoa(cpf=cpf)
    assert p1.cpf == cpf
