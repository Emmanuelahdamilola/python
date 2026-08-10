def unique_tags(tags):
    cleaned = []
    for tag in tags:
        tag = tag.strip().lower()
        if tag and tag not in cleaned:
            cleaned.append(tag)
    return sorted(cleaned)