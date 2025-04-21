# To Do List Program

my_list = []


def add_task():
    task = input("enter a new task: ")
    my_list.append({"Task": task, "Status": "pending"})
    print("New Task Added \n")


def remove_task():
    if len(my_list) == 0:
        print("list is empty!")
    else:
        try:
            search_index = int(input("Enter the task number to be removed: ")) - 1
            if 0 <= search_index < len(my_list):
                removed_task = my_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid Task Number!")
        except ValueError:
            print("Enter Valid Task Number")


def view_task():
    if len(my_list) == 0:
        print("No Tasks")
    else:
        print("Your To-Do List of Tasks:")
        for index, task in enumerate(my_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")


def mark_completed():
    if len(my_list) == 0:
        print("List is Empty")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as completed: ")) - 1
            if 0 <= search_index < len(my_list):
                my_list[search_index]['Status'] = 'completed'
                print(f"Task {my_list[search_index]['Task']} marked as completed")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Enter a Valid Task Number \n ")


def menu():
    while True:
        print("**** To-Do-List Application ****")
        print("1. Add a new Task")
        print("2. Remove a Task")
        print("3. View the Tasks")
        print("4. Mark the Task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print(" Task to be Added ")
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Exit..")
            exit()
        else:
            print("Invalid Choice!")


menu()

