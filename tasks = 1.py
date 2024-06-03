tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully!")
    else:
        print(f"Task '{task}' not found in the list.")

def display_tasks():
    if tasks:
        print("Tasks in the to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the to-do list.")

while True:
    print("\nSelect an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

