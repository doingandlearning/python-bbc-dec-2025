# test_expenses.py

import pytest

from expenses import (
    MoneyParseError,
    parse_gbp_to_pence,
)


# ---------------------------------------------------------
# parse_gbp_to_pence: small, pure function tests
# ---------------------------------------------------------

@pytest.mark.parametrize(
    "raw, expected_pence",
    [
        ("0", 0),
        ("1", 100),
        ("1.0", 100),
        ("1.00", 100),
        ("12.3", 1230),
        ("12.34", 1234),
        ("£12.34", 1234),
        ("  £  12.34  ", 1234),
        ("-0.50", -50),
        ("-12.34", -1234),
    ],
)
def test_parse_gbp_to_pence_valid_strings(raw, expected_pence):
    assert parse_gbp_to_pence(raw) == expected_pence


def test_parse_gbp_to_pence_accepts_int_pence():
    assert parse_gbp_to_pence(1234) == 1234


@pytest.mark.parametrize("raw", ["", "abc", "£", "12.345", "12,34", "£12.3.4"])
def test_parse_gbp_to_pence_rejects_invalid_strings(raw):
    with pytest.raises(MoneyParseError):
        parse_gbp_to_pence(raw)


def test_parse_gbp_to_pence_rejects_float_to_avoid_rounding():
    with pytest.raises(TypeError):
        parse_gbp_to_pence(12.34)

