#!/usr/bin/python3
"""
Script that, using thi REST API, for a given employee ID, returns information about his/her TODO list progress
"""

import csv
import requests
import sys

if __name__ == "__main__":
  user_url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
  task_url = "https://jsonplaceholder.typicode.com/todos"
  user_id = int(sys.argv[1])
  filename = sys.argv[1] + ".csv"

  user_name = (requests.get(user_url)).json().get("username")
  tasks = requests.get(task_url)

  with open(filename, "w", newline='') as csv_file:
    csv_wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for task in tasks.json():
      if (task.get("userId") == user_id):
        title = task.get("title")
        status = task.get("completed")
        csv_wr.writerow([str(user_id), user_name, status, title])