def solution(name, a, b, c):
    Sum = a + b + c
    Average = round(Sum / 3, 2)
    Maximum = max(a, b, c)
    return f"Student: {name}\nSum: {Sum}\nAverage: {Average}\nMaximum: {Maximum}"