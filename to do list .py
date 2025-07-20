import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        file.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            task = input("Enter new task: ")
            tasks.append(f"[ ] {task}")
            save_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == '4':
            show_tasks(tasks)
            index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= index < len(tasks):
                if tasks[index].startswith("[ ]"):
                    tasks[index] = tasks[index].replace("[ ]", "[✔]")
                    save_tasks(tasks)
                else:
                    print("Task already completed.")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
