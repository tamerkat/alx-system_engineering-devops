#!/usr/bin/python3
'''
Write a Python script
'''
import csv
import requests
from sys import argv


def shown():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break

    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUM_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))

    filename = "{}.csv".format(argv[1])
    with open(filename, mode="w") as fc:
        fcw = csv.writer(fc)
        fcw.writerow(["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        fcw.writerows(TASK_TITLE)


if __name__ == '__main__':
    shown()
