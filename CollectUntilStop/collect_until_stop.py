def collect_until_stop(items):
    result = []
    
    for item in items:
        cleaned_item = item.strip().lower()
        if cleaned_item == "stop":
            break
        result.append(item)

    return result