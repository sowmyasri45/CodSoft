# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if tasks:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("No tasks found.")

# Function to delete a task
def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Main function to interact with the user
def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Complete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            delete_task(index)
        elif choice == '4':
            index = int(input("Enter the task index to mark as completed: "))
            complete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()