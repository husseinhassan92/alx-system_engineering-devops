#!/usr/bin/python3
"""
Request from API; Return TODO dict progress given employee ID
"""
import json
import requests
from sys import argv


def to_json():
    """return API data"""
    r_users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in r_users.json():
        if user['id'] == int(argv[1]):
            EMPLOYEE_NAME = user['username']

    TASKS = []
    r_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in r_todo.json():
        if todo['userId'] == int(argv[1]):
            TASKS.append((todo['completed'], todo['title']))

    list = []
    for TASK in TASKS:
        list.append({"task": TASK[1], "completed": TASK[0],
                     "username": EMPLOYEE_NAME})

    filename = "{}.json".format(argv[1])
    with open(filename, 'w') as file:
        json.dump({argv[1]: list}, file)


if __name__ == "__main__":
    to_json()
