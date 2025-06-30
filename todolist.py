import os

TODO_FILE = 'todo.txt'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        f.writelines(task + '\n' for task in tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\nOptions: add, remove, quit")
        cmd = input("Enter command: ").lower()
        if cmd == 'add':
            task = input("New task: ")
            tasks.append(task)
        elif cmd == 'remove':
            num = int(input("Task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
        elif cmd == 'quit':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
