def set_comparison(a, b):
    set_a = set(a)
    set_b = set(b)

    both = set_a & set_b

    only_a = set_a - set_b
    only_b = set_b - set_a
    
    only_a = sorted(list(only_a))
    only_b = sorted(list(only_b))
    both = sorted(list(both))
    return {"both": both, "only_a": only_a, "only_b": only_b}

    pass
