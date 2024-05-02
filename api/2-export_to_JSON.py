#!/usr/bin/python3
"""
Module that export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    id = int(argv[1])
    emp_data = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    usr_name = emp_data.json().get('username')
    tasks_data = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    data_all = [boole for boole in tasks_data.json()
                if boole.get('userId') == id]

    list_json = [{
        "task": data['title'],
        "completed": data['completed'],
        "username": usr_name
    } for data in data_all]

    with open(str(id) + ".json", "a", encoding="utf-8") as file:
        dic_employess = {}
        dic_employess[f"{id}"] = list_json
        json.dump(dic_employess, file)
