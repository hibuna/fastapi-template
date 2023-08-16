def pascal_to_capital(pascal: str) -> str:
    """Convert Pascal case to capitalized."""
    capital = f"{pascal[0]}"
    for c in pascal[1:]:
        s = " " if c.isupper() else ""
        capital += s + c
    return capital
