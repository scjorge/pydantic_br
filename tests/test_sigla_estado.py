import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import SiglaEstado, FieldInvalidError, FieldTypeError

sigla_estado_mock = [
    "AC",
    "AL",
    "AM",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "DF",
    "ES",
    "GO",
    "GO",
    "MA",
    "MG",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "PR",
    "RJ",
    "RN",
    "RO",
    "RR",
    "RS",
    "SC",
    "SE",
    "SP",
    "TO",
]


@pytest.fixture
def endereco():
    class Endereco(BaseModel):
        sigla_estado: SiglaEstado

    yield Endereco


@pytest.mark.parametrize("sigla_estado", sigla_estado_mock)
def test_must_be_string(endereco, sigla_estado):
    p1 = endereco(sigla_estado=sigla_estado)
    assert isinstance(p1.sigla_estado, str)


@pytest.mark.parametrize("sigla_estado", sigla_estado_mock)
def test_must_accept_only_numbers(endereco, sigla_estado):
    p1 = endereco(sigla_estado=sigla_estado)
    assert p1.sigla_estado == sigla_estado


@pytest.mark.parametrize("sigla_estado", sigla_estado_mock)
def test_must_fail_when_use_another_type(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        endereco(sigla_estado=[sigla_estado])
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("sigla_estado", sigla_estado_mock)
def test_must_fail_when_use_invalid_sigla_estado(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        invalid_sigla_estado = "Z" + sigla_estado[1]
        endereco(sigla_estado=invalid_sigla_estado)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("sigla_estado", sigla_estado_mock)
def test_must_fail_when_use_digits_count_above_sigla_estado(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        endereco(sigla_estado=sigla_estado * 2)
    assert FieldInvalidError.msg_template in str(e.value)
