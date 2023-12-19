#!/usr/bin/python3
"""
This module uses Python to make requests to a REST API.
fix
It fetches data about a specific employee's tasks
and prints a summary of the tasks completed and the
titles of the completed tasks.
"""
import requests
import sys

# Get ID from command line
id = sys.argv[1]

# Get user name
user = requests.get('https://jsonplaceholder.typicode.com/users/' + id)

# Convert to JSON
data = user.json()

# Get name
name = data['name']

# Get todos
todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + id)

# Convert to JSON
todos_data = todos.json()

# Get total number of todos
total = str(len(todos_data))

# Get number of completed todos
completed = str(sum([1 for task in todos_data if task['completed'] is True]))

# Print Employee 'name' is done with tasks('completed'/'total'):
print('Employee {} is done with tasks({}/{}):'.format(name, completed, total))

# Print title of completed tasks
for task in todos_data:
    if task['completed'] is True:
        print('\t {}'.format(task['title']))

if __name__ == '__main__':
    pass
