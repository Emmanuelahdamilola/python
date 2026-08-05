def vote_eligibility(age, country):
    if age >= 18 and country.strip().title() == "Nigeria":
        return "Eligible"
    else:
        return "Not eligible"
    pass
