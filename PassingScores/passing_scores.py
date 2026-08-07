def passing_scores(scores, minimum):
    result = []

    for score in scores:
        if score >= minimum:
            result.append(score)
    return result
    pass