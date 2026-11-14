import sys
import os
import json

exists = os.path.exists("tasks.json")

Initial_task = []
filtering_tasks = ["done","todo","inprogress"]

def read_data() -> list:
    with open("tasks.json","r") as file:
        data = json.load(file)

    return data

#Method to write data to json
def write_data(data) -> None:
    with open("tasks.json","w") as file:
        json.dump(data,file, indent=2)

def read_data(status = None) -> list:
    with open("tasks.json","r") as file:
        data = json.load(file)
    
    required_tasks = []

    if status == None:
        return data

    if status == 1:
        for task in data:
            if task["status"] == "todo":
                required_tasks.append(task)
    elif status == 2:
        for task in data:
            if task["status"] == "done":
                required_tasks.append(task)
    elif status == 3:
        for task in data:
            if task["status"] == "inprogress":
                required_tasks.append(task)
    
    return required_tasks

def print_data(status = None) -> None:
    with open("tasks.json","r") as file:
        data = json.load(file)

    no_of_task = len(data)
    if no_of_task < 1:
        print("Empty list")
    elif status == None:
        for i in range(no_of_task):
            print(f"{i+1}. {data[i]}")
    elif status == 1:
        for task in data:
            if task["status"] == "todo":
                print(task)
    elif status == 2:
        for task in data:
            if task["status"] == "done":
                print(task)
    elif status == 3:
        for task in data:
            if task["status"] == "inprogress":
                print(task)
    
def print_clean(task_list):
    no_of_task = len(task_list)
    if no_of_task < 1:
        print("Empty list")
    else:
        for i, task in enumerate(task_list):
            print(f"{i+1}. Task: {task['description']} | Status: {task['status']}")

#Checks if file exists
if exists:
    list_of_tasks = read_data()
else:
    with open("tasks.json","w") as file:
        json.dump(Initial_task,file, indent=2)
        list_of_tasks = []

n = len(sys.argv) - 1
digit_set = {"0","1","2","3","4","5","6","7","8","9"}


if n < 1:
    print("Invalid Command")

elif "add" == sys.argv[1] and n >= 2:
    print("Command: ", sys.argv[1])
    secondArg = " ".join(sys.argv[2:])
    print("Task: ", secondArg)
    list_of_tasks.append({"description":secondArg, "status": "todo"})
    write_data(list_of_tasks)
    print_data()

elif "delete" == sys.argv[1]:
    no_of_task = len(list_of_tasks)
    print_data()
    print("Enter task you want to delete (number/type 'clear' for all the done tasks)")
    choice = input(": ")
    int_choice = choice != "" and set(choice).issubset(digit_set)
    if int_choice and int(choice) > 0 and int(choice) <= no_of_task:
        list_of_tasks.pop(int(choice)-1)
        write_data(list_of_tasks)
        print_data()
    elif choice.lower() == "clear":
        for task in list_of_tasks:
            if task["status"] == "done":
                index = list_of_tasks.index(task)
                list_of_tasks.pop(index)
        write_data(list_of_tasks)
        print_data()
    else:
        print("Invalid Choice")

elif "update" == sys.argv[1]:
    print("Command: ", sys.argv[1])
    print("Select which list you want to update \n1. To Do\n2. Done\n3. In Progress")
    choice = int(input(": "))
    if choice in {1,2,3}:
        required_tasks = read_data(choice)
        print_clean(required_tasks)
    print("Enter task you want to change status")
    choice = input(": ")
    required_task = required_tasks[int(choice)-1]
    print("Enter the status update \n1. To Do\n2. Done\n3. In Progress")
    print(f"Choice cannot be {required_task['status']}!!!")
    choice = int(input(": "))
    if choice in {1,2,3}:
        if choice == 1:
            required_task["status"] == "todo"
            change = "todo"
        elif choice == 2:
            required_task["status"] == "done"
            change = "done"
        else:
            required_task["status"] == "inprogress"
            change = "inprogress"

    for task in list_of_tasks:
        if task["description"] == required_task["description"]:
            task["status"] = change

    write_data(list_of_tasks)
    print_data() 
    

elif "list" == sys.argv[1] and n == 1:
    print_data()

elif "list" == sys.argv[1] and n >=2 :
    secondArg = " ".join(sys.argv[2:])
    if secondArg == "todo":
        print_data(1)
    elif secondArg == "done":
        print_data(2)
    elif secondArg == "in progress":
        print_data(3)
    else:
        print("Invalid task list")

    
elif "list" == sys.argv[1] and n == 2:
    data = read_data()
    totalTasks = len(data)
    if totalTasks < 1:
        print("Empty list")
    is_digit = sys.argv[2] != "" and set(sys.argv[2]).issubset(digit_set)
    if is_digit:
        id = int(sys.argv[2])
        if id in list_of_tasks:
            print(f"Task ID {id}: {list_of_tasks[id]}")
    else:
        print("Invalid Command")
else:
    print("Invalid Command")





