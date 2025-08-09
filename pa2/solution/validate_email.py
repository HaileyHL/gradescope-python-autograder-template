def validate_email(email_address,email_suffix):
    email = email_address.strip()
    email_parts = email.split("@")
    if len(email_parts) != 2:
        return False
    for part in email_parts:
        if " " in part:
            return False
    return email_parts[2] == email_suffix
