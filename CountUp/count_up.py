def count_up(n):
    if n < 1:
        return []
    
    result = []
    for num in range(1, n + 1):
        result.append(num)
    return result