from pydantic import BaseModel, validator

from pydantic_br.fields import CPF


class Pessoa(BaseModel):
    nome: str
    cpf: CPF(mask="mask1")


    # @validator("cpf", always=True)
    # def not_valid_ip(cls, v):
    #     raise ValueError(f'Invalid CPF:: {v}')

p1 = Pessoa(cpf=True, nome='kk')
print(p1)


def test_cpf_criate():
    assert 1 == 1
