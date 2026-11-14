import sys
import os
import json

exists = os.path.exists("tasks.json")

Initial_task = []

def read_data() -> list:
    with open("tasks.json","r") as file:
        data = json.load(file)

    return data

#Method to write data to json
def write_data(data) -> None:
    with open("tasks.json","w") as file:
        json.dump(data,file, indent=2)

def print_data():
    data = read_data()
    totalTasks = len(data)
    if totalTasks < 1:
        print("Empty list")
    else:
        for i in range(totalTasks):
            print(f"{i+1}. {data[i]}")
    


#Checks if file exists
if exists:
    list_of_tasks = read_data()
else:
    with open("tasks.json","w") as file:
        json.dump(Initial_task,file, indent=2)
        list_of_tasks = []

#Initialization of required variables
filtering_list = ["done", "todo", "inprogress"]
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
    totalTasks = len(list_of_tasks)
    print("Command: ", sys.argv[1])
    if totalTasks < 1:
        print("Empty List of Tasks")
    else:    
        print_data()
        print("Select which task to delete (number/type 'clear' to delete all the done): ")
        choice = input(" : ")
        if choice != "" and set(choice).issubset(digit_set):
            print("Number only")
        elif choice.lower() == "clear":
            print("clear")
        else:
            print("Invalid Choice")


elif "update" == sys.argv[1] and n == 3:
    print("Command: ", sys.argv[1])
    print("Number: ", sys.argv[2])
    print("Task: ", sys.argv[3])

elif "list" == sys.argv[1] and n == 1:
    print_data()

elif "list" == sys.argv[1] and n >=2 :
    secondArg = sys.argv[2]
    if secondArg == "todo":
        print(list_of_tasks)
    elif secondArg == "done":
        pass

    
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





