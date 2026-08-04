def safe_calculator(a, operator, b):
    if (operator == "/" or operator == "%") and b == 0:
        return "Cannot divide by zero"
    elif operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return round(a / b, 2)
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a ** b
    else:
        return "Invalid operator"
    pass
