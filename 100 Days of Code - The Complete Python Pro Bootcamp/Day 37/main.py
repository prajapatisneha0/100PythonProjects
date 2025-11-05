import requests
from datetime import datetime
import os

TOKEN =os.environ.get("SHEET_TOKEN")
USERNAME = os.environ.get("SHEET_USERNAME")
GRAPH_ID= "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# TODO 1 Create User USING POST
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# TODO Create Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Get today's date in YYYYMMDD format
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_data ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data , headers=headers)
print(response.text)

# TODO create put methode
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2"
}
response = requests.delete(url=update_endpoint,json=new_pixel_data , headers=headers)
print(response.text)

# TODO create delete methode

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)