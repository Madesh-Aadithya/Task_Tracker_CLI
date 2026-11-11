import sys
import os
import json

exists = os.path.exists("tasks.json")

Initial_task = []

if exists:
    with open("tasks.json","r") as file:
        list_of_tasks = json.load(file)
else:
    with open("tasks.json","w") as file:
        json.dump(Initial_task,file)
        list_of_tasks = []

filtering_list = ["done", "todo", "inprogress"]



n = len(sys.argv) - 1
no_of_task = len(list_of_tasks)
digit_set = {"0","1","2","3","4","5","6","7","8","9"}



if n < 1:
    print("Invalid Command")

elif "add" == sys.argv[1] and n >= 2:
    print("Command: ", sys.argv[1])
    print("Task: ", sys.argv[2:])
    list_of_tasks[no_of_task+1] = {"description":sys.argv[2:], "status": "todo"}
    write_data(list_of_tasks)
    no_of_task = len(list_of_tasks)
    print(list_of_tasks)

elif "delete" == sys.argv[1] and n == 2:
    print("Command: ", sys.argv[1])
    if no_of_task < 1:
        print("Empty List of Tasks")
    else:    
        is_digit = sys.argv[2] != "" and set(sys.argv[2]).issubset(digit_set)
        if is_digit and int(sys.argv[2]) in list_of_tasks:
            list_of_tasks.pop(int(sys.argv[2]))
        else:
            print("Task Not found")
        print(list_of_tasks)



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



def write_data(data) -> None:
    with open("tasks.json","w") as file:
        json.dump(data,file)

