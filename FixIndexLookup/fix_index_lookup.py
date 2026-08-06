def get_item(items, index):
    if index < 0 or index >= len(items):
        return "Index out of range"
    return items[index]
    pass
