from pydantic import BaseModel

from pydantic_br import CPFMask


class Pessoa(BaseModel):
    cpf: CPFMask
    nome: str


p1 = Pessoa(nome="João", cpf=["532.213.947-80"])
