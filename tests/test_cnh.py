def test_must_be_string(person, cnh):
    ...


def test_mascara_must_be_string(person_masks, cnh):
    ...


def test_digits_must_be_string(person_digits, cnh):
    ...


def test_must_accept_with_mask(person_masks, cnh):
    ...


def test_must_accept_only_numbers(person_digits, cnh):
    ...


def test_must_fail_when_use_mask_in_digits_class(person_masks, cnh):
    ...


def test_must_fail_when_use_digits_in_mask_class(person_digits, cnh):
    ...


def test_must_fail_when_use_another_type(person_digits, cnh):
    ...


def test_must_fail_when_use_invalid_cnhs(person, cnh):
    ...


def test_must_fail_when_use_digits_count_above_cnhs(person, cnh):
    ...


def test_must_fail_when_use_digits_count_below_cnhs(person, cnh):
    ...


def test_must_fail_when_use_sequecial_digits(person, cnh):
    ...
