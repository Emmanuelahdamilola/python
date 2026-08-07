def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"

    total = 0
    for num in range(1, limit + 1):
        if num % divisor == 0:
            total += num
    return total