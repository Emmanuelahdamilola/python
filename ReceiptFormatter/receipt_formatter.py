import email


def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)
    subtotal = round(quantity * float(price), 2)
    tax = round(subtotal * 0.075, 2)
    total = round(subtotal + tax, 2)
    return f"Customer: {name}\nSubtotal: {subtotal}\nTax: {tax}\nTotal: {total}"
    pass


student = {
    "Name": "Emmanuel",
    "Age": 25,
    "Email" : "emmanuel@example.com",
    "courses": ["Python", "SQL", "Django"]    
}

print(student["Email"])

student["courses"].append("Data Science")

student["courses"].remove("SQL")

"Python" in student["courses"]

student["Age"] = 26
student["courses"].append("JavaScript")
print("Django" in student["courses"])

for course in student["courses"]:
    print(course)
    
