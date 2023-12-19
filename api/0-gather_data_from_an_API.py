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

    employee_id = int(sys.argv[1])
    # Fetch user data
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    if not user_data:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    EMPLOYEE_NAME = user_data["name"]
    # Fetch user's TODO list
    todo_url = f"{base_url}/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate TODO list and completed todo list
    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    NUMBER_OF_DONE_TASKS = sum(task["completed"] for task in todo_data)

    # Display progress information
    print(f"Employee {EMPLOYEE_NAME} is done with tasks "
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Display titles of completed tasks
    completed_tasks = [task["title"]
                       for task in todo_data if task["completed"]]

    for TASK_TITLE in completed_tasks:
        print(f"\t{TASK_TITLE}")
