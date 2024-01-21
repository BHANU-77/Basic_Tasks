tasks = []

def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

def add_new_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

def mark_as_done(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

def remove_existing_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

while True:
    print("\nOptions:")
    print("1. Show to-do list")
    print("2. Add a new task")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_new_task(task_name)
    elif choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to mark as done: "))
        mark_as_done(task_number)
    elif choice == '4':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_existing_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
