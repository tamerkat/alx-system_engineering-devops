#!/usr/bin/python3
'''
display
'''

import sys
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    usr_id = sys.argv[1]

    for user in users.json():
        if user.get('id') == usr_id:
            EMPLOYEE_NAME = users['name']
            break

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    url = 'https://jsonplaceholder.typicode.com/todos'
    todo = requests.get(url)

    for task in todo:
        if task.get('completed') == "True":
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
            TASK_TITLE.append(task.get('title'))
        else:
            TOTAL_NUMBER_OF_TASKS += 1
            TASK_TITLE.append(task.get('title'))

    avrage = NUMBER_OF_DONE_TASKS / TOTAL_NUMBER_OF_TASKS
    print("Employee {} is done with tasks({}):".format(EMPLOYEE_NAME, avrage))

    for task in TASK_TITLE:
        print("\t {}".format(task))
