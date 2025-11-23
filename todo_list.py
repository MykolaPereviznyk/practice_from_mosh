choice = "Enter your choice"
task = "Enter your task!"
new_task = "Enter a new task"


def print_menu(data):
    print("-------------------------------------------")
    print("Todo List Menu: ")
    viev_task(data)


def viev_task(data):
    print("-------------------------------------------")
    if data:
        for index, task in enumerate(data, start=1):
            print(f"{index}. {task}")
    else:
        print("Empty")
    print("-------------------------------------------")


def get_choice(text, data):
    while True:
        try:
            user_input = input(f"{text}: ")
            if user_input.isdigit() and inlist(user_input, data) or text == new_task:
                if user_input:
                    return user_input
            raise ValueError
        except ValueError:
            print(f"Invalid {text}")


def inlist(user_input, data):
    if 0 < int(user_input) <= len(data):
        return True
    return False


def add_task(tasks):
    viev_task(tasks)
    user_input = get_choice(new_task, tasks)
    tasks.append(user_input)
    return tasks


def remove_task(tasks):
    viev_task(tasks)
    user_input = get_choice(task, tasks)
    if inlist(user_input, tasks):
        tasks.pop(int(user_input) - 1)
        return tasks


def main():
    todo_list = ["Grecery shopping", "Reading"]
    data = ("View Tasks", "Add a Task", "Remove a Task", "Exit")

    while True:
        print_menu(data)

        user_int = get_choice(choice, data)
        if user_int == "1":
            viev_task(todo_list)
        elif user_int == "2":
            todo_list = add_task(todo_list)
        elif user_int == "3":
            todo_list = remove_task(todo_list)
        elif user_int == "4":
            break


if __name__ == "__main__":
    main()
