# A simple To-Do List Application in Python

# Initialize an empty list to store the tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

# Function to display the to-do list
def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to update a task
def update_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_num = int(input("\nEnter the task number you want to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num - 1] = new_task
        print(f"Task {task_num} updated to '{new_task}'.")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_num = int(input("\nEnter the task number you want to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted from the to-do list.")
    else:
        print("Invalid task number!")

# Main function to run the to-do list application
def to_do_list_app():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

# Run the to-do list application
to_do_list_app()
