def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("Список пуст")
    else:
        for i, task in enumerate(tasks, start=1):
            print(i, task)


def add_task(tasks):
    task = input("Введите задачу: ")
    tasks.append(task)
    save_tasks(tasks)


def del_task(tasks):
    try:
        index = int(input("Введите номер задачи: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except (ValueError, IndexError):
        print("Ошибка")


def search_tasks(tasks):
    word = input("Введите слово: ")
    found = False

    for task in tasks:
        if word.lower() in task.lower():
            print(task)
            found = True

    if not found:
        print("Не найдено")



tasks = load_tasks()

while True:
    print("\n1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Найти задачу")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        del_task(tasks)
    elif choice == "4":
        search_tasks(tasks)
    elif choice == "5":
        break