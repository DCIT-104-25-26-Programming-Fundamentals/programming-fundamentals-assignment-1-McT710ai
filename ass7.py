def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "=" * 30)
    print("     TO-DO LIST MENU")
    print("=" * 30)
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("-" * 30)


def add_task(tasks):
    """
    Ask user for a task description and add it to the list.
    """
    task = input("Enter task: ").strip()
    if task:  # Don't add empty tasks
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task description cannot be empty.")


def view_tasks(tasks):
    """
    Display all tasks with their numbers.
    """
    if not tasks:
        print("Your task list is empty. Add some tasks!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(tasks):
    """
    Show tasks, ask for a number, and remove that task.
    """
    if not tasks:
        print("Your task list is empty. Nothing to delete!")
        return
    
    # Show current tasks
    view_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        
        # Check if the number is valid (1-based index)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print(f"Error: Task number {task_num} does not exist.")
            
    except ValueError:
        print("Error: Please enter a valid number.")


def main():
    """
    Main program loop that runs the to-do list application.
    """
    tasks = []  # Initialize empty task list
    
    while True:
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice (1-4): ").strip()
        
        # Process the choice
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break  # Exit the loop and end the program
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


# Run the program
if __name__ == "__main__":
    main()