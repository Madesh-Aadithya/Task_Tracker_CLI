import os
import json

exists = os.path.exists("tasks.json")

task_list = [{"description":"Fix Car", "status":"Todo"},
             {"description":"Fix Bike", "status":"Todo"}]

data = []

if exists:
    print("File exist")
    with open("tasks.json", "r") as file:
        data = json.load(file)
else:
    print("File does not exist")
    with open("tasks.json", "w") as file:
        json.dump(task_list, file)
        data = task_list


print(data)