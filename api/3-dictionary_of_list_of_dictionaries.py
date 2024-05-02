#!/usr/bin/python3
"""
Module that export data in the JSON format.
"""
import json
import requests

if __name__ == '__main__':
    tasks_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    users_id = list(set([ids['userId'] for ids in tasks_data]))
    dic = {}
    for usrId in users_id:

        emp_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{usrId}').json()

        emp_data = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{usrId}/todos').json()

        list_data = [{
            "username": emp_name['username'],
            "task": data['title'],
            "completed": data['completed']
        } for data in emp_data]
        dic[usrId] = list_data

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(dic, file)