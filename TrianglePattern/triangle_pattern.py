def triangle_pattern(n):
    if n < 1:
        return ""

    result = []
    for row in range(1, n + 1):
        row = "*" * row
        result.append(row)
    result = "\n".join(result)

    return result
    
