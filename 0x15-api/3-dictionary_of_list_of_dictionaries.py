#!/usr/bin/python3
"""
Request from API; Return TODO dict progress for all employees
"""
import json
import requests


def to_json():
    """return API data"""
    data = {}
    r_users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in r_users.json():
        USER_id = user['id']
        EMPLOYEE_NAME = user['username']

        TASKS = []
        r_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
        for todo in r_todo.json():
            if todo['userId'] == USER_id:
                TASKS.append((todo['completed'], todo['title']))

        list = []
        for TASK in TASKS:
            list.append({"task": TASK[1], "completed": TASK[0],
                         "username": EMPLOYEE_NAME})

        data[USER_id] = list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(data, file, sort_keys=True)


if __name__ == "__main__":
    to_json()
