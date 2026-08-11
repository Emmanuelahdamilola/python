def initials_badge(full_name):
    words = full_name.strip().split()
    
    letters = []
    for word in words:
        letters.append(word[0].upper())
    
    return ".".join(letters) + "."