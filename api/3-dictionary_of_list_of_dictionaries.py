#!/usr/bin/python3
"""script using a REST API,
   returns information about all tasks from all employees
   export data to json format.
"""

import json
import requests

if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{BASE_URL}/users").json()
    dict_users_task = {}
    for user in users:
        tasks = requests.get(f"{BASE_URL}/users/{user['id']}/todos").json()
        dict_users_task[user["id"]] = []
        for task in tasks:
            dict_task = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            dict_users_task[user["id"]].append(dict_task)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_task, file)
