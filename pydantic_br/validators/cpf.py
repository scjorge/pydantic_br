import re

__all__ = ["validate_cpf"]

def _get_cpf_numbers(cpf):
    cpf = re.sub("[^0-9]", "", str(cpf))

def validate_cpf_data(cpf): ...

def validate_cpf(cpf):

    cpf = _get_cpf_numbers()

    invalid_list = [
        "00000000000",
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999",
    ]

    if cpf in invalid_list:
        return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calcula o primeiro digito """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight
        weight = weight - 1

    check_digit = 11 - sum % 11

    if check_digit > 9:
        first_digit = 0
    else:
        first_digit = check_digit

    """ Calcula o segundo digito """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight
        weight = weight - 1

    check_digit = 11 - sum % 11

    if check_digit > 9:
        second_digit = 0
    else:
        second_digit = check_digit

    if cpf[-2:] == "%s%s" % (first_digit, second_digit):
        return True
    return False
