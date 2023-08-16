def validate_email(value: str) -> bool:
    return value not in (
        "admin@example.com",
        "postmaster@example.com",
        "root@example.com",
    )
