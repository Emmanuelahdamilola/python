def group_by_first_letter(names):
    result = {}

    for name in names:
        name = name.strip()

        if not name:
            continue

        letter = name[0].upper()

        if letter not in result:
            result[letter] = []

        result[letter].append(name)

    return result