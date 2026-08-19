def bunk_assignment(service_number):
    shifted = service_number - 1
    room = (shifted // 8) + 1
    bunk = (shifted % 8) + 1
    return f"Room {room}, Bunk {bunk}"
    pass
