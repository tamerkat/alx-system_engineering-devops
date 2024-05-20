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
            USERNAME = (user.get('username'))
            break

    TASK_TITLE = []

    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_TITLE.append(todo.get('completed'),
                              todo.get('title'))

    filename = "{}.csv".format(argv[1])
    with open(filename, mode="w") as cf:
        csvfile = csv.writer(cf)
        csvfile.writerow(["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in TASK_TITLE:
            csvfile.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                              "TASK_COMPLETED_STATUS": task['completed'],
                              "TASK_TITLE": task['title']})


if __name__ == "__main__":
    shown()
