from pydantic import BaseModel

from pydantic_br.fields import CPF


class Pessoa(BaseModel):
    cpf: CPF(mask="mask1")
    cpf1: CPF(mask="mask2")


p1 = Pessoa(cpf=[44], cpf1="jorge")
print(p1.dict())


def test_cpf_criate():
    assert 1 == 1
