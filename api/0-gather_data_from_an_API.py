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

    employee_name = user_data["name"]
    # Fetch user's TODO list
    todo_url = f"{base_url}/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate TODO list and completed todo list
    total_tasks = len(todo_data)
    done_tasks = sum(task["completed"] for task in todo_data)

    # Display progress information
    print(f"Employee {employee_name} is done with tasks "
          f"({done_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    completed_tasks = [task["title"]
                       for task in todo_data if task["completed"]]

    for task_title in completed_tasks:
        print(f"\t{task_title}")
