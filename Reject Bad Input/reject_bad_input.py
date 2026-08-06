def solution(value):
    try:
        num = float(value)
    except(ValueError):
        return "Invalid number"
    return round(num * 2, 2)