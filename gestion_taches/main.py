tasks = []

def display_menu():
    print("\n--- Todo list ---")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Modify a task")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Quit")
 
def add_task():
     name = input("Enter the name of the task : ")
     priority = input("Enter the priority of the task (1-5)").capitalize()
     tasks.append({"name": name, "priority": priority})
     print(f"Task '{name}' added successfully.")
     
def display_tasks():
    if not tasks:
        print("No task found.")
    else:
        print("\n--- List of tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} - Priority: {task['priority']}")
            
def modify_tasks():
    display_tasks()
    try:
        index = int(input("Enter the number of the task to modify :")) -1
        if 0 <= index < len(tasks):
            task[index]["name"] = input("Enter the new name of the task : ")
            task[index]["priority"] = input("Enter the new priority of the task (1-5) : ").capitalize()
            print("Task modified successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_task():
    display_tasks()
    try:
        index = int(input("Enter the number of the task to delete : ")) -1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task '{deleted_task['name']}' deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")
        
def save_tasks():
    file_name = input("Enter the name of the file to save the tasks (default: tasks.txt) : ") or "tasks.txt"
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task['name']} - Priority: {task['priority']}\n")
    print(f"Tasks saved to {file_name}.")
    
def load_tasks():
    file_name = input("Enter the name of the file to Load the tasks (default: tasks.txt)") or "tasks.txt"
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            tasks.clear()
            for line in lines:
                name, priority = line.strip().split(" - Priority: ")
                tasks.append({"name": name, "priority": priority})
            print(f"Tasks loaded from {file_name}.")          
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        
def quit_program():
    print("Thank you for using the Todo list app. Goodbye!")
    exit()
    
while True:
    display_menu()
    choice = input("Enter your choice (1-7) : ")
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        modify_tasks()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        load_tasks()
    elif choice == "7":
        quit_program()
    else:
        print("Invalid choice. Please try again.")
            



