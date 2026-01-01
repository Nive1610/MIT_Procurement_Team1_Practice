import re

def validate_user(data):
    username = data.get("username", "")
    password = data.get("password", "")

    if len(username) < 7:
        return False, "Username must be at least 7 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[@#$]", password):
        return False, "Password must contain at least one special character (@, #, or $)."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    return True, "Registration successful!"
