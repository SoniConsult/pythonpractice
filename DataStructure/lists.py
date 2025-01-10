
def todo_list():
    tasks = {} 
    print("Welcome to the To-Do List!")
    print("Choose an option:")
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1': 
            task_id = len(tasks) + 1
            task_description = input("Enter the task description: ")
            tasks[task_id] = {'task': task_description, 'status': 'pending'}
            print(f"Task '{task_description}' added with ID {task_id}.")

        elif choice == '2': 
            print("\nTo-Do List:")
            if not tasks:
                print("No tasks found.")
            else:
                for task_id, task_info in tasks.items():
                    print(f"ID: {task_id}, Task: {task_info['task']}, Status: {task_info['status']}")

        elif choice == '3':  
            task_id = int(input("Enter the task ID to mark as done: "))
            if task_id in tasks:
                tasks[task_id]['status'] = 'done'
                print(f"Task ID {task_id} marked as done.")
            else:
                print(f"Task ID {task_id} not found.")

        elif choice == '4': 
            task_id = int(input("Enter the task ID to update: "))
            if task_id in tasks:
                new_description = input("Enter the new task description: ")
                tasks[task_id]['task'] = new_description
                print(f"Task ID {task_id} updated.")
            else:
                print(f"Task ID {task_id} not found.")

        elif choice == '5': 
            task_id = int(input("Enter the task ID to delete: "))
            if task_id in tasks:
                del tasks[task_id]
                print(f"Task ID {task_id} deleted.")
            else:
                print(f"Task ID {task_id} not found.")

        elif choice == '6':  
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
todo_list()
