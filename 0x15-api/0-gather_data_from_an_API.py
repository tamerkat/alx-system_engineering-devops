#!/usr/bin/python3
'''
display
'''

import sys
import requests


def show():
    """shown"""
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    for user in users.json():
        if user.get('id') == int(sys.argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    show()
