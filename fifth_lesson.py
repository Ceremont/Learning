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
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    operation = input("Enter operation: ")
    result = calculate(number1, number2, operation)
    return result
print(run_calculator())
