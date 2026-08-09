import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import SiglaEstado, FieldInvalidError, FieldTypeError
from pydantic_br.validators.sigla_estado_validator import SIGLAS


@pytest.fixture
def endereco():
    class Endereco(BaseModel):
        sigla_estado: SiglaEstado

    yield Endereco


@pytest.mark.parametrize("sigla_estado", SIGLAS)
def test_must_be_string(endereco, sigla_estado):
    p1 = endereco(sigla_estado=sigla_estado)
    assert isinstance(p1.sigla_estado, str)


@pytest.mark.parametrize("sigla_estado", SIGLAS)
def test_must_accept_only_numbers(endereco, sigla_estado):
    p1 = endereco(sigla_estado=sigla_estado)
    assert p1.sigla_estado == sigla_estado


@pytest.mark.parametrize("sigla_estado", SIGLAS)
def test_must_fail_when_use_another_type(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        endereco(sigla_estado=[sigla_estado])
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("sigla_estado", SIGLAS)
def test_must_fail_when_use_invalid_sigla_estado(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        invalid_sigla_estado = "Z" + sigla_estado[1]
        endereco(sigla_estado=invalid_sigla_estado)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("sigla_estado", SIGLAS)
def test_must_fail_when_use_digits_count_above_sigla_estado(endereco, sigla_estado):
    with pytest.raises(ValidationError) as e:
        endereco(sigla_estado=sigla_estado * 2)
    assert FieldInvalidError.msg_template in str(e.value)

def test_there_must_be_27_values_in_siglas():
    """We only have 26 states and 1 federal district"""
    assert len(SIGLAS) == 27
