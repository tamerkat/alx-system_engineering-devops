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
            if todo.get('completed') is True:
                TASK_TITLE.append(todo.get('title'))

    filename = "{}.csv".format(argv[1])
    with open(filename, mode="w") as csvfile:
        for todo in todos:
            complete = todo.get('completed')
            title = todo.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, USERNAME, complete, title))


if __name__ == "__main__":
    shown()
