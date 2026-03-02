
def greet(name):
    return f"Hello, {name}"

print(greet("Danielo"))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def calculate(a,b,operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    return None

print(is_even(15))
print(calculate(5,2,"*"))
