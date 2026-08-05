def password_strength(password):
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    if len(password) >= 8 and has_letter and has_digit:
        return "Strong"
    elif len(password) >= 8:
        return "Medium"
    else:
        return "Weak"
