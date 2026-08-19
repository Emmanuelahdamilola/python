def muster_record(name, service_number):
    shifted = service_number - 1
    room = (shifted // 8) + 1
    bunk = (shifted % 8) + 1
    return f"RECRUIT: {name}\nSERVICE NUMBER: {service_number}\nQUARTERS: Room {room}, Bunk {bunk}"
    pass
