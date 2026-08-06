def exact_calculator(left, operator, right):
    try:
        left = int(left)
        right= int(right)
    except (ValueError):
        return "Invalid number"
    
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"
    if (operator == "/" or operator == "%") and right == 0:
        return "Cannot divide by zero"
    
    if operator == "+":
        return round(left + right, 2)
    elif operator == "-":
        return round(left - right, 2)
    elif operator == "*":
        return round(left * right, 2)
    elif operator == "/":
        return round(left / right, 2)
    elif operator == "%":
        return round(left % right, 2)
    elif operator == "**":
        return round(left ** right, 2)
    pass
