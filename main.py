name = input("give name: ")
age = int(input("give age: "))

print(f"Привет, {name}, через год тебе будет {age + 1}")

if age < 18:
    print("Молодняк")
else:
    print("Старик")


# calculator
try:
    liczba1 = int(input("give liczba 1: "))
    liczba2 = int(input("give liczba 2: "))
except ValueError:
    print("Буквы, не цифры")
    exit()

choice = input("выбери действие (+, -, *, /): ")

if choice == "+":
    print(liczba1 + liczba2)
elif choice == "-":
    print(liczba1 - liczba2)
elif choice == "*":
    print(liczba1 * liczba2)
elif choice == "/":
    if liczba2 == 0:
        print("Деление на ноль нельзя")
    else:
        print(liczba1 / liczba2)
else:
    print("Неизвестная операция")