def contact_lookup(contact, key):
    if key not in contact:
        return "Not found"
    return contact[key]
    pass