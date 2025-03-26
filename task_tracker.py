import json #importing JSON module for file storage

#initialising task list and a counter for unique tasks IDs

tasks = [] #task list
task_id_counter = 1 #counter for unique task IDs

def save_tasks():
    with open('tasks.json', 'w') as file: #opening the file in write mod
        json.dump(tasks,file,indent=4)

def load_tasks():
    global tasks, task_id_counter #accessing the global task list
    try:
        with open("tasks.json","r") as file:
            tasks = json.load(file) #loading tasks from the file
        if tasks:
            task_id_counter = max(task["id"] for task in tasks)+1 #Update counter    
    except (FileNotFoundError, json.JSONDecodeError):
        tasks=[] # If file doesnt exist, initialise empty list

#defining function to add tasks

def add_task():
    """
    title(str)
    description(str)
    status(str): default: 'pending'
    """
    global task_id_counter
    
    title = input("Enter task title:").strip()
    description = input("Enter task description:").strip()
    
    if not title:
        print("Task title cannot be empty")
        return
    
    #creating task dictionary
    task={
        'id': task_id_counter,
        'title': title,
        'description':description,
        'status': status
    }
    tasks.append(task)
    task_id_counter += 1 #incrementing task ID counter
    save_tasks() #saving the task list to the file
    print(f"Task '{title}' added successfully!")
    
#defining function to view tasks

def view_tasks():
    """
    Displays all the tasks
    """
    if not tasks:
        print("No tasks available!")
        return
    print("\nTask List:")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - {task['status']}")
        
#defining function to update tasks

def update_task():
    
    """
    Updates the status of a task based on its ID.
    
    Parameters:
        task_id (int): The unique ID of the task to update.
        new_status (str): The new status of the task.
    """
    if not tasks:
        print("No tasks to update!\n")
        return
    
    try:
        task_id = int(input("Enter the task ID to update:"))
        new_status = input("Enter new status (Pending/Completed):").strip().capitalize()
        
        if new_status not in ["Pending", "Completed"]:
            print("Error: Invalid status! Please enter 'Pending' or 'Completed'")
            return
        
        for task in tasks:
            if task['id'] == task_id:
                task['status']  = new_status
                save_tasks()
                print(f"Task {task_id} updated successfully to {new_status}!")
                return
        
        print("Task not found!")
    
    except ValueError:
        print("Error: Invalid task ID! Please enter a valid integer.\n")

#defining function to delete tasks
    
def delete_task():
    """
    Deletes a task from the task list based on its ID.
    
    Parameters:
        task_id (int): The unique ID of the task to delete.
    """
    if not tasks:
        print("No tasks to delete!\n")
        return
    
    try:
        task_id = int(input("Enter the task ID to delete:"))
        
        tasks
        filtered_tasks=[task for task in tasks if task["id"]!=task_id]
        if len(filtered_tasks) == len(tasks):
            print("Task not found!\n")
            return
        
        tasks.clear()
        tasks.extend(filtered_tasks)
        save_tasks()
        print(f"Task {task_id} deleted successfully!")
    
    except ValueError:
        print("Error: Invalid task ID! Please enter a valid integer.\n")
        
def show_menu():
    while True:
        print("\n📌 Task Tracker Menu:")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Update Task Status")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")
        
        choice = input("Enter your choice (1-5):").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Task Tracker. Goodbye!")   
            break
        else:
            print("Error: Invalid choice found, please enter number between 1-5")

load_tasks()

show_menu()
    



