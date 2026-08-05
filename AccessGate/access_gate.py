def access_gate(age, has_id, is_banned):
    if age < 18:
        return "Too young"
    elif has_id == False:
        return "No ID"
    elif is_banned == True:
        return "Banned"

    return "Allowed"