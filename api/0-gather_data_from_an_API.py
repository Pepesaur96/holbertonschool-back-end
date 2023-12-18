#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URL for the employee's TODO list
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Make a GET request to the API
        response = requests.get(todo_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            todos = response.json()

            # Get the employee's name
            employee_name = todos[0]['username'] if todos else "Unknown"

            # Count the number of completed tasks
            completed_tasks = [todo for todo in todos if todo['completed']]
            num_completed_tasks = len(completed_tasks)

            # Display employee information
            print(
                f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{len(todos)}):")

            # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")
        else:
            print(
                f"Error: Unable to fetch TODO list. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line
    employee_id = int(sys.argv[1])

    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)
