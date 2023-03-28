from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf: CPF()


def test_cpf_must_be_string():
    cpf = "000.000.000-00"
    p1 = Pessoa(cpf=cpf)
    assert isinstance(p1.cpf, str)


def test_cpf_must_accept_with_mask():
    ...


def test_cpf_must_accept_only_numbers():
    ...
