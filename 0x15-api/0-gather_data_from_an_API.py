import requests
import sys

def  fetch_employee_todo_ptogress(employee_id):
  #Define the URLs
  base_url = "https://jsonplaceholder.typicode.com"
  user_url = f"{base_url}/users/{employee_id}"
  todo_url = f"{base_url}/todos?userId={employee_id}"

  #Fetch employee data
  user_response = requests.get(user_url)
  if user_response.status_code != 200:
    print(f"Error: Employee with ID {employee_id} not found.")
    return
  user_data = user_response.json()
  employee_name = user_data.get("name")

  #Fetch TODO list data for the employee
  total_tasks = len(todos)
  completed_tasks = [task for task in todos if task["completed"]]
  number_of_done_tasks = len(completed_tasks)

  #Display the progress
  print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
  for task in completed_tasks:
    print("\t", task["title"])

  #Check if an employee ID was provided as a comand-line argument
  if __name__ == "__main__":
    if len(sys.argv) != 2:
      print("Usage: python script.py <employee_id>")
    else:
      try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_ptogress(employee_id)
      except ValueError:
        print("Error: Please enter a valid integer for employee ID.")