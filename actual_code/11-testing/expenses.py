import re

_MONEY_RE = re.compile(r"^\s*£?\s*([+-]?\d+)(?:\.(\d{1,2}))?\s*$")

class MoneyParseError(ValueError):
    pass

def parse_gbp_to_pence(value) :
    """
    Convert a GBP amount to integer pence.

    Accepts:
      - "12.34", "£12.34", "12", "12.3", "-0.99"
      - int pence (already)
    Returns:
      - int pence

    Raises:
      - TypeError for unsupported types
      - MoneyParseError for invalid strings
    """
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        raise TypeError("Use strings or ints for money to avoid float rounding issues")

    if not isinstance(value, str):
        raise TypeError(f"Unsupported money type: {type(value).__name__}")

    m = _MONEY_RE.match(value)
    if not m:
        raise MoneyParseError(f"Invalid money string: {value!r}")

    pounds_str, pennies_str = m.group(1), m.group(2)

    pounds = int(pounds_str)
    pennies = int((pennies_str or "0").ljust(2, "0"))

    # Handle negative amounts like "-0.50" correctly
    sign = -1 if pounds_str.strip().startswith("-") else 1
    return pounds * 100 + sign * pennies