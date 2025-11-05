import requests
import os

sheet_endpoint = "https://api.sheety.co/94ebf60eebfe883f1d4d228b5439218b/flightWorksheet/prices"
AUTH_TOKEN =os.environ.get ("FLIGHT_AUTH_TOKEN")

class DataManager:

    def __init__(self):
        self.username = os.environ.get("USERNAME")
        self.password = os.environ.get("PASSWORD")
        self.authorization = AUTH_TOKEN
        self.destination_data = {}

    def get_data(self):
        #  use the sheety api to get all data
        response = requests.get(url=sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # in datamanager class make put request and row id from sheet_data
    # to upadte the google sheet with IATA code

    def update_code(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheet_endpoint} / {city["id"]}",
                json= new_data,
                auth= self.authorization
            )
            print(response.text)


