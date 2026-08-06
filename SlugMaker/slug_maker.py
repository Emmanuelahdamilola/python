def slug_maker(title):
    return title.strip().lower().replace(" ", "-").replace(",", "").replace(".", "")
    pass
