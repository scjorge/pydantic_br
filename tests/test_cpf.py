from pydantic import BaseModel

from pydantic_br import CPF


class Pessoa(BaseModel):
    cpf: CPF()


def test_cpf_must_be_string():
    cpf = '000.000.000-00'
    p1 = Pessoa(cpf=cpf)
    assert p1.cpf == cpf
