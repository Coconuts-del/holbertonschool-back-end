#!/usr/bin/python3
"""script using a REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
        sys.exit(1)

    EMPLOYEE_ID = int(sys.argv[1])
    # Fetch user data
    BASE_URL = "https://jsonplaceholder.typicode.com/users"
    USER_URL = f"{BASE_URL}/{EMPLOYEE_ID}"

    # Fetch user data
    USER_RESPONSE = requests.get(USER_URL)
    USER_DATA = USER_RESPONSE.json()
    if not USER_DATA:
        print(f"Employee with ID {EMPLOYEE_ID} not found.")
        sys.exit(1)

    EMPLOYEE_NAME = USER_DATA["name"]
    # Fetch user's TODO list
    TODO_URL = f"{BASE_URL}/{EMPLOYEE_ID}/todos"
    TODO_RESPONSE = requests.get(TODO_URL)
    TODO_DATA = TODO_RESPONSE.json()

    # Calculate TODO list and completed todo list
    TOTAL_NUMBER_OF_TASKS = len(TODO_DATA)
    # NUMBER_OF_DONE_TASKS = sum(task["completed"] for task in TODO_DATA)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in TODO_DATA:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])

    # Display progress information
    print(f"Employee {EMPLOYEE_NAME} is done with tasks "
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Display titles of completed tasks
    for title in TASK_TITLE:
        print("\t ", title)
