tasks = []

while True:
    print("\n===== To-Do Application =====")
    print("1. View all tasks")
    print("2. Add a new task.")
    print("3. Mark a task as completed.")
    print("4. Remove a task.")
    print("5. View all Completed tasks.")
    print("6. View all pending tasks.")
    print("0. For exit.")
    
    option = int(input("Enter your desired option no.: "))

    if option == 1:
        print("\nYour added tasks:")

        for index, task in enumerate(tasks):
            print(f"----- {index}: {task['name']} - {task['is_completed']}")

    elif option == 2:
        value = input("Enter a new task: ")
        task = {'name':value, 'is_completed': False}
        tasks.append(task)

        print(f"{value} - Added successfully.")

    elif option == 3:
        choice = int(input("Enter the task's id you want to mark as completed: "))
        tasks[choice]['is_completed'] = True

        print(f"{tasks[choice]['name']} is successfully completed.")

    elif option == 4:
        choice = int(input("Enter the task's id to remove: "))

        tasks.pop(choice)
        print(f"{tasks[choice]['name']} is removed successfully.")
    
    elif option == 5:
        print("\nYour completed tasks")

        for index, task in enumerate(tasks):
            if task['is_completed'] == True:
                print(f"-----{index}: {task['name']}")
            else:
                continue
    
    elif option == 6:
        print("\nYour pending tasks")

        for index, task in enumerate(tasks):
            if task['is_completed'] == False:
                print(f"-----{index}: {task['name']}")
            else:
                continue
    
    elif option == 0:
        print("Good Bye...")
        break

    else:
        print("You have entered an invalid option.\nPlease, Try Again.")