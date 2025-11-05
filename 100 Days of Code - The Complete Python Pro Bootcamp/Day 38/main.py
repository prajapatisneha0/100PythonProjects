import requests
from datetime import datetime
import os

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "female"
WEIGHT_KG = 48
HEIGHT_CM = 163
AGE = 19

API_ID = os.environ.get("NTR_API_ID")
API_KEY = os.environ.get("NTR_API_KEY")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("tell me which exercises you did:")

headers ={
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": text,
    "gender": GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(exercise_endpoint,json=exercise_params,headers=headers)
result = response.json()
# print(f"Nutritionix API call: \n {result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

YOUR_TOKEN = os.environ.get("SHEET_AUTH_TOKEN")
USERNAME = os.environ.get("NTRI_USERNAME")
PASSWORD = os.environ.get("NTRI_PASSWORD")

GOOGLE_SHEET_NAME = "sheet1"
sheet_endpoint = os.environ.get("NTRI_SHEET_ENDPOINT")

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
           "calories": exercise["nf_calories"]
        }
    }
    """
       sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
       """

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth = (
            USERNAME,
            PASSWORD,
        )
    )

    """
    bearer_headers = {
        "Authorization":f"Bearer {YOUR_TOKEN}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json= sheet_inputs,
        headers=bearer_headers,
    )
    """


    print(f"Sheety Response : \n {sheet_response.text}")


