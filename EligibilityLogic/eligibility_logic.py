def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill == True:
        return "Eligible"
    else:
        return "Not eligible"
    pass

print(eligibility_logic(75, 85, True))