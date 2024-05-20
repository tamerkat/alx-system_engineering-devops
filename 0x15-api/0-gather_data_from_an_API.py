#!/usr/bin/python3
'''
display
'''

import requests
import sys

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    usr_id = int(sys.argv[1])
    EMPLOYEE_NAME = None

    for user in users.json():
        if user.get('id') == usr_id:
            EMPLOYEE_NAME = (user.get('name'))
            break

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    url = 'https://jsonplaceholder.typicode.com/todos'
    todo = requests.get(url)

    for task in todo.json():
        if task.get('userId') == usr_id:
            TOTAL_NUMBER_OF_TASKS += 1

            if task.get('completed') == "True":
                NUMBER_OF_DONE_TASKS += 1
                TOTAL_NUMBER_OF_TASKS += 1
                TASK_TITLE.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))
