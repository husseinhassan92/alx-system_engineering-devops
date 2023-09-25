#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import csv
import requests
from sys import argv


def to_csv():
    """return API data"""
    r_users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in r_users.json():
        if user['id'] == int(argv[1]):
            EMPLOYEE_NAME = user['name']

    TASKS = []
    r_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in r_todo.json():
        if todo['userId'] == int(argv[1]):
            TASKS.append((todo['completed'], todo['title']))

    filename = '{}.csv'.format(argv[1])
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for TASK in TASKS:
            writer.writerow([argv[1], EMPLOYEE_NAME, TASK[0], TASK[1]])


if __name__ == "__main__":
    to_csv()
