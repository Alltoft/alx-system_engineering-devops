#!/usr/bin/python3
"""a Python script that, using jsonplaceholder.typicode REST API,
for a given userloyee ID, returns information about his/her
TODO list progress and  export data in the CSV format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json().get("username")

    all_in_all = []
    request = requests.get('https://jsonplaceholder.typicode.com//todos')\
        .json()

    for task in request:
        if (task.get("userId") == int(user_id)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = user_name
            all_in_all.append(temp)

    with open("{}.json".format(user_id), "a") as f:
        json.dump({user_id: all_in_all}, f)
