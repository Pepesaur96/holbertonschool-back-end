#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


id = sys.argv[1]
user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
data = user.json()
name = data['name']
todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + id)
todos_data = todos.json()
total = str(len(todos_data))
completed = str(sum([1 for task in todos_data if task['completed'] is True]))

print('Employee {} is done with tasks({}/{}):'.format(name, completed, total))

for task in todos_data:
    if task['completed'] is True:
        print('\t {}'.format(task['title']))

if __name__ == '__main__':
    pass
