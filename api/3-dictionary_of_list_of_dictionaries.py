#!/usr/bin/python3
import json
import requests

if __name__ == '__main__':
    emp_data = requests.get('https://jsonplaceholder.typicode.com/users/')
    tasks_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    dic = {}
    for employees in emp_data.json():
        list_data = []
        for all_data in tasks_data.json():
            if employees.get('id') == all_data.get('userId'):
                list_data.append({
                    "task": all_data['title'],
                    "completed": all_data['completed'],
                    "username": employees['name']
                })
                dic[f"{employees['id']}"] = list_data
    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(dic, file)
