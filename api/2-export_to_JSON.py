#!/usr/bin/python3
"""script using a REST API, for a given employee ID,
   returns information about his/her TODO list progress
   export data to json.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
        sys.exit(1)

    BASE_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = int(sys.argv[1])

    EMPLOYEE_TODOS = requests.get(f"{BASE_URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    TODO_DATA = EMPLOYEE_TODOS.json()

    username = TODO_DATA[0]["user"]["username"]
    USER_TASK = {EMPLOYEE_ID: []}
    fileName = f"{EMPLOYEE_ID}.json"
    for task in TODO_DATA:
        dict_task = {"task": task["title"], "completed": task["completed"],
                     "username": username}
        USER_TASK[EMPLOYEE_ID].append(dict_task)
    with open(fileName, "w") as file:
        json.dump(USER_TASK, file)
