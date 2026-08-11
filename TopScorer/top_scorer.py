def top_scorer(scores):
    if not scores:
        return "No scores"

    top_name = None
    top_score = None

    for name, score in scores.items():
        if top_score is None or score > top_score:
            top_score = score
            top_name = name
        elif score == top_score and name < top_name:
            top_name = name

    return top_name