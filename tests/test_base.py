from pydantic import BaseModel, __version__
import pytest

from pydantic_br import (
    CPF,
    CNH,
    CPFMask,
    CPFDigits,
    CNPJ,
    CNPJDigits,
    CNPJMask,
    TE,
    PIS,
    PISMask,
    PISDigits,
    Certidao,
    CertidaoMask,
    CertidaoDigits,
)


@pytest.fixture(scope="session")
def model():
    class GeneralModel(BaseModel):
        cpf: CPF = "661.554.170-08"
        cpf_mask: CPFMask = "661.554.170-08"
        cpf_digits: CPFDigits = "66155417008"
        cnh: CNH = "49761142867"
        cnpj: CNPJ = "80.680.038/0001-91"
        cnpj_digits: CNPJDigits = "80680038000191"
        cnpj_mask: CNPJMask = "80.680.038/0001-91"
        te: TE = "526340880167"
        pis: PIS = "977.75868.13-5"
        pis_mask: PISMask = "977.75868.13-5"
        pis_digits: PISDigits = "97775868135"
        certidao: Certidao = "13324601552017174927061644649830"
        certidao_mask: CertidaoMask = "133246.01.55.2017.1.74927.061.6446498.30"
        certidao_digits: CertidaoDigits = "13324601552017174927061644649830"

    general_model = GeneralModel()
    return general_model


def test_model_schemas(model: BaseModel):
    if __version__.startswith("2"):
        model.model_dump()
        model.model_dump_json()
        model.model_json_schema()
    if __version__.startswith("1"):
        model.dict()
        model.schema()
