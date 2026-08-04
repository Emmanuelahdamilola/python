def str_len(value):
    if value == "":
        return 0
    return 1 + str_len(value[1:])
    pass