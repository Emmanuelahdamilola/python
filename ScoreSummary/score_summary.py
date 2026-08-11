def score_summary(name, a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid score"
    
    if a < 0 or a > 100 or b < 0 or b > 100 or c < 0 or c > 100:
        return "Invalid score"

    average = round((a + b + c) / 3, 2)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
    return f"Student: {name}\nAverage: {average}\nGrade: {grade}"
    pass
