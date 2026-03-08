numbers = [5, 8, 2, 17, 4]
print(numbers[0])
print(numbers[-1])
print(len(numbers))
# task 2
numbers.append(99)
print(numbers)
numbers.pop(2)
print(numbers)
# task 3
for number in numbers:
    print(number)
# task 4
for number in numbers:
    if number > 5:
        print(number)
# task 5
print(sum(numbers))
# mini chalenge
names = ["Alex", "Bob", "Anna", "Artem", "Mike"]

nameA = []
for name in names:
    if name.startswith("A"):
        nameA.append(name)
print(nameA)

# dictionaries
user = {
    "name": "Alex",
    "age": 20,
    "city": "Warsaw"
}
print(user["name"])
print(user["age"])
print(user["city"])
# 2
user["age"] = 21
print(user["age"])
# 3
user['job'] = 'Python developer'
print(user['job'])
print(user)
# 4
for value in user.values():
    print(value)
# 5
print(user.get("country"))
# 6
users = [
    {"name": "Alex", "age": 20},
    {"name": "Anna", "age": 17},
    {"name": "Mike", "age": 25}
]
for user in users:
    if user["age"] > 18:
        print(user["name"])

# func
def Hello():
    print("Hello")

# 2
def greet(name):
    return f"Hello {name}"

print(greet("Danielo"))
# 3
def add(a, b):
    return a + b
print(add(1, 2))
# 4
def is_adult(age):
    return age >= 18
# 5
def get_max(numbers):
    return max(numbers)
# 6
users = [
    {"name": "Alex", "age": 20},
    {"name": "Anna", "age": 17},
    {"name": "Mike", "age": 25}
]
def show_adult(users):
    for user in users:
        if user["age"] >= 18:
            print(user)
print(show_adult(users))