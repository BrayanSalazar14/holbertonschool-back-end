#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    id = int(argv[1])
    emp_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    usr_name = emp_data.json().get('name')

    tasks_data = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    comp_tasks = [data["userId"] for data in tasks_data.json()
                  if data["completed"] is True].count(id)

    all_tasks = [data["userId"] for data in tasks_data.json()].count(id)

    titles = [title['title'] for title in tasks_data.json()
              if title['completed'] is True and title['userId'] == id]

    print(f"Employee {usr_name} is done with tasks({comp_tasks}/{all_tasks}):")

    for title in titles:
        print("\t ", title)
