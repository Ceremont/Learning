import random
number = random.randint(1, 100)
attempts = 0
while True:
    try:
        guess = input("Guess a number between 1 and 100: ")
        guess = int(guess)
    except ValueError:
        print("ЧИСЛА")
        continue
        attempts += 1
    if number == guess:
        print("Браво,угадал")
        break
    elif number < guess:
        print("Меньше")
    elif number > guess:
        print("Больше")
print(f"Ты угадал за {attempts} попыток")