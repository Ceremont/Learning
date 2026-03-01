name = input("give name:")
age = int(input("give age:"))
print(f"Привет, {name}, через год тебе будет {age + 1}")
if age <= 18:
    print("Молодняк")
else:
    print("Старик")

# calc
try:
    liczba1 = int(input("give liczba 1:"))
    liczba2 = int(input("give liczba 2:"))
except ValueError:
    print("Буквы,не цифры")
choice = input("выбери действие калькулятора(+,-,*,/)")
suma = liczba1 + liczba2
minus = liczba1 - liczba2
umnoz = liczba1 * liczba2
dele = int (liczba1) / int (liczba2)
if choice == "+":
    print(suma)
elif choice == "-":
    print(minus)
elif choice == "*":
    print(umnoz)
elif choice == "/":
    print(dele)
