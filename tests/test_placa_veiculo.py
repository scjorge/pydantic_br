import pytest
from pydantic import BaseModel, ValidationError

from pydantic_br import PlacaVeiculo, FieldInvalidError, FieldTypeError

placa_mock = [
    "KCY6475",
    "MND5684",
    "AYD7808",
    "GSY5845",
    "JME4383",
    "CBQ5968",
    "JFL0428",
    "HPH4896",
    "NEH4545",
    "ICN2737",
    "ABC1D23",
    "XYZ9A87",
    "LMN2B34",
    "PQR3C56",
    "GHI4D89",
    "JKL5E01",
    "RST6F23",
    "UVW7G45",
    "OPQ8H67",
    "DEF9I90",
]


@pytest.fixture
def car():
    class Car(BaseModel):
        placa: PlacaVeiculo

    yield Car


@pytest.mark.parametrize("placa", placa_mock)
def test_must_be_string(car, placa):
    p1 = car(placa=placa)
    assert isinstance(p1.placa, str)


@pytest.mark.parametrize("placa", placa_mock)
def test_must_fail_when_use_another_type(car, placa):
    with pytest.raises(ValidationError) as e:
        car(placa=[placa])
    assert FieldTypeError.msg_template in str(e.value)


@pytest.mark.parametrize("placa", placa_mock)
def test_must_fail_when_use_invalid_placa(car, placa):
    with pytest.raises(ValidationError) as e:
        invalid_placa = placa[0] + placa[:5] + placa[6:]
        car(placa=invalid_placa)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("placa", placa_mock)
def test_must_fail_when_use_invalid_placa_fist_digit(car, placa):
    with pytest.raises(ValidationError) as e:
        invalid_placa = placa[1:] + "0"
        car(placa=invalid_placa)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("placa", placa_mock)
def test_must_fail_when_use_digits_count_above_placa(car, placa):
    with pytest.raises(ValidationError) as e:
        car(placa=placa * 2)
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize("placa", placa_mock)
def test_must_fail_when_use_digits_count_below_placa(car, placa):
    with pytest.raises(ValidationError) as e:
        car(placa=placa[:5])
    assert FieldInvalidError.msg_template in str(e.value)


@pytest.mark.parametrize(
    "placa",
    [
        "000000000000000",
        "111111111111111",
        "222222222222222",
        "333333333333333",
        "444444444444444",
        "555555555555555",
        "666666666666666",
        "777777777777777",
        "888888888888888",
        "999999999999999",
    ],
)
def test_must_fail_when_use_sequecial_digits(car, placa):
    with pytest.raises(ValidationError) as e:
        car(placa=placa)
    assert FieldInvalidError.msg_template in str(e.value)
