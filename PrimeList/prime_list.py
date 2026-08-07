def prime_list(n):
    result = []

    for num in range(2, n + 1):
        is_prime = True

        for is_prime in range(2, num):
            if num % is_prime == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result
