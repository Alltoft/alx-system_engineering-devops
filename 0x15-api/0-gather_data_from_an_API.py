#!/usr/bin/python3
"""a Python script that, using jsonplaceholder.typicode REST API,
for a given employee ID, returns information about his/her
TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(emp_id)).json().get("name")
    Num_of_task = 0
    tasks_done = []

    request = requests.get('https://jsonplaceholder.typicode.com//todos')\
        .json()

    for test in request:
        if test.get('userId') == int(emp_id):
            Num_of_task += 1
            if test.get('completed') is True:
                tasks_done.append(test.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(emp_name, len(tasks_done), Num_of_task))
    for task_title in tasks_done:
        print('\t {}'.format(task_title))
