#!/usr/bin/python3
"""script using a REST API, for a given employee ID,
   returns information about his/her TODO list progress
   export data in the CSV format.
"""

import csv
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
    EMPLOYEE_NAME = TODO_DATA[0]["user"]["username"]

    fileName = f"{EMPLOYEE_ID}.csv"
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in TODO_DATA:
            writer.writerow(
                [EMPLOYEE_ID, EMPLOYEE_NAME, str(task["completed"]),
                 task["title"]]
            )
