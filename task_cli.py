import sys
import os
import json

exists = os.path.exists("tasks.json")

Initial_task = []

#Method to write data to json
def write_data(data) -> None:
    with open("tasks.json","w") as file:
        json.dump(data,file, indent=2)

def read_data() -> list:
    with open("tasks.json","r") as file:
        data = json.load(file)
    return data

def print_data() -> None:
    with open("tasks.json","r") as file:
        data = json.load(file)

    no_of_task = len(data)

    if no_of_task < 1:
        print("Empty list")
    else:
        for i in range(no_of_task):
            print(f"{i+1}. {data[i]}")
    

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


elif "update" == sys.argv[1] and n == 3:
    print("Command: ", sys.argv[1])
    print("Number: ", sys.argv[2])
    print("Task: ", sys.argv[3])

elif "list" == sys.argv[1] and n == 1:
    print("Listing done Tasks: ........")

elif "list" == sys.argv[1] and n >=2 :
    secondArg = sys.argv[2]
    if secondArg == "todo":
        print(list_of_tasks)
    elif secondArg == "done":
        pass

    
elif "list" == sys.argv[1] and n == 2:
    if no_of_task < 1:
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





