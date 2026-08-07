def chunk_list(items, size):
    if size < 1:
        return "Invalid size"
    
    result = [items[i: i + size] for i in range(0, len(items), size)]
    return result
    