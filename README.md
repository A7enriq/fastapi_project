FastAPI Client with Requests
Introduction
This project is a simple Python client that communicates with a FastAPI application using the Requests library.
It allows users to retrieve items, add new items, and delete existing items through HTTP requests.
Features
Get all items from the API.
Add a new item to the list.
Delete an item from the list.
Handle API responses.
Check HTTP status codes.
Technologies
Python
Requests
FastAPI
REST API
API Endpoints
MethodEndpointDescriptionGET/getitems/Get all itemsPOST/add/{new_item}Add a new itemDELETE/deleteitem?item={item}Delete an item 
Project Structure
project/ ├── main.py └── app_api.py 
Installation
Install the required library:
pip install requests 
How to Run
Start the FastAPI server.
Make sure the API is running on http://127.0.0.1:8000.
Run the Python client:
python main.py 
Usage
The client sends HTTP requests to the FastAPI server.
get_all_items() retrieves all items.
add_item(new_item) adds a new item.
delete_item(item) removes an existing item.
The API response is returned as JSON.
Error Handling
The project checks the HTTP response status code and returns an error message if the request fails.
Author
Python Programming Student
