tasks = []

def show_menu():
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added.")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks found.")
        
        else:
            print("\nYour To-Do List: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("📭 No tasks to remove")

        else:
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num -1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("❌ Invalid task number.")

            except ValueError:
                print("❌ please enter a valid number")
    
    elif choice == "4":
        print("Goodbye! 👋")
        break
