def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)
    subtotal = round(quantity * float(price), 2)
    tax = round(subtotal * 0.075, 2)
    total = round(subtotal + tax, 2)
    return f"Customer: {name}\nSubtotal: {subtotal}\nTax: {tax}\nTotal: {total}"
    pass
