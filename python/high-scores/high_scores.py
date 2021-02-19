def latest(scores):
    return scores[-1]
    pass


def personal_best(scores):
    scores.sort()
    return scores[-1]
    pass


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores if len(scores) <= 3 else list(scores[:3])
    pass
