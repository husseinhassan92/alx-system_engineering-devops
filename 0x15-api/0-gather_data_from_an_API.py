#!/usr/bin/python3

import requests
from sys import argv


def display():
    """"""
    r_users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in r_users.json():
        if user['id'] == int(argv[1]):
            EMPLOYEE_NAME = user['name']

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASKS = []
    r_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in r_todo.json():
        if todo['userId'] == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
        if todo['userId'] == int(argv[1]) and todo['completed']:
            NUMBER_OF_DONE_TASKS += 1
            TASKS.append(todo['title'])
    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for TASK in TASKS:
        print('\t {}'.format(TASK))


if __name__ == "__main__":
    display()
