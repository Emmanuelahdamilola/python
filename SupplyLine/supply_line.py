def supply_line(item, quantity, unit_weight):
    # Calculate the total weight
    total_weight = quantity * unit_weight
    
    # Use float normalization (removing floating-point artifacts like .000000001)
    # The g format specifier removes trailing zeros and precision anomalies
    unit_weight_str = f"{unit_weight:g}"
    total_weight_str = f"{total_weight:g}"
    
    if '.' not in unit_weight_str:
        unit_weight_str += '.0'
    if '.' not in total_weight_str:
        total_weight_str += '.0'

    return f"{quantity} x {item} @ {unit_weight_str}kg = {total_weight_str}kg"
