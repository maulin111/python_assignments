# Get requests
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/100')
print(response.status_code)
print(response.json())
print(response.headers)
# POST requests
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1,"title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# response.json()
# print(response.json())

