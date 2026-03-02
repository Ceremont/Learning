def greet(name):
    return f"Hello, {name}"

print(greet("Danielo"))

def is_even(number):
    return number % 2 == 0

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error"
        return a / b
    else:
        return "Unknown operation"

def run_calculator():
    try:
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter another number: "))
    except ValueError:
        return "Invalid number"

    operation = input("Enter operation: ")
    return calculate(number1, number2, operation)
print(run_calculator())
def calculate_many(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate_many(1, 2, 3))
def power(number,exponent=2):
    return number ** exponent
print(power(2,15))
def create_user(name, age, country="Unknown"):
    return f"Name: {name}, Age: {age}, Country: {country}"
print(create_user(age=25, name="Daniel", country="Poland"))
def create_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
def make_order(produkt,price,quantity=1,**extras):
    total = price * quantity
    for value in extras:
        total += extras[value]
    return total
print(make_order("Phone", 500, quantity=2, delivery=20, case=10))