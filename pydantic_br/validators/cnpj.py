import re

__all__ = [
    "validate_cnpj",
    "validate_cnpj_mask",
]


def validate_cnpj_mask(cnpj: str) -> bool:
    if len(cnpj) == 18:
        if (
            cnpj[2:3] == "."
            and cnpj[6:7] == "."
            and cnpj[10:11] == "/"
            and cnpj[15:16] == "-"
        ):
            return True
    return False


def validate_cnpj(cnpj: str) -> bool:
    if not isinstance(cnpj, str):
        return False

    cnpj = re.sub("[^0-9]", "", cnpj)

    if len(cnpj) != 14:
        return False

    sum = 0
    weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    """ Valida o primeiro digito """
    for n in range(12):
        value = int(cnpj[n]) * weight[n]
        sum = sum + value

    check_digit = sum % 11

    if check_digit < 2:
        first_digit = 0
    else:
        first_digit = 11 - check_digit

    """ Valida o segundo digito """
    sum = 0
    weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for n in range(13):
        sum = sum + int(cnpj[n]) * weight[n]

    check_digit = sum % 11

    if check_digit < 2:
        second_digit = 0
    else:
        second_digit = 11 - check_digit

    if cnpj[-2:] == "%s%s" % (first_digit, second_digit):
        return True
    return False
