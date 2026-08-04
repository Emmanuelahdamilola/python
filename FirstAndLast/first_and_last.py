def first_and_last(value):
    if value:
        return {"last": value[0], "first": value[-1]}
    else:
        return {"last": "", "first": ""}