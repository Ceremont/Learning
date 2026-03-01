tasks = []
while True:
    print("\n1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        if not tasks:
            print("Список пуст")
        else:
            for i, task in enumerate(tasks):
                print(i, task)

    elif choice == "2":
        task = input("Введите задачу: ")
        tasks.append(task)

    elif choice == "3":
        try:
            index = int(input("Введите номер задачи: "))
            tasks.pop(index)
        except ValueError:
            print("Ошибка")

    elif choice == "4":
        break