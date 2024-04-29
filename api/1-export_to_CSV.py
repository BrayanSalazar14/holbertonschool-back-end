#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    id = int(argv[1])
    emp_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    usr_name = emp_data.json().get('name')

    tasks_data = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    all_tasks = [data["userId"] for data in tasks_data.json()]

    task_data = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    titles = [title['title'] for title in task_data.json()
              if title['completed'] is True and title['userId'] == id]

    for title in titles:
        print("\t ", title)