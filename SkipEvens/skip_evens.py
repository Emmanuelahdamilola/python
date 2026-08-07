def skip_evens(start, end):
    if start > end:
        return []
    
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            continue
        result.append(num)
    return result
        