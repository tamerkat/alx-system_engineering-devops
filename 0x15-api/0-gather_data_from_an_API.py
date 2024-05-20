#!/usr/bin/python3
'''
display
'''

import urllib
from sys import arvg

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = urllib.request.urlopen(url)

    usr_id = sys.argv[1]

    for user in users:
        if user['id'] == usr_id:
            EMPLOYEE_NAME = users['name']
            break

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    url = 'https://jsonplaceholder.typicode.com/todos/1'
    todo = urllib.request.urlopen(url)

    for task in todo:
        if task['completed'] == 'True':
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
            TASK_TITLE.append(task['title'])
        else:
            TOTAL_NUMBER_OF_TASKS += 1

    avrage = NUMBER_OF_DONE_TASKS / TOTAL_NUMBER_OF_TASKS
    print("Employee {} is done with tasks({}):".format(EMPLOYEE_NAME, avrage))

    for task in TASK_TITLE:
        print("\t {}".format(task))
