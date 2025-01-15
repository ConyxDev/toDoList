print("Welcome to the todo list project")

tasks = []

def display_menu():
    print("\n--- Todo list ---")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Modify a task")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Quit")
 
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
            
  
    
            


