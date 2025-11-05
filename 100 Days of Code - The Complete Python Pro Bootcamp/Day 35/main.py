import requests
import smtplib
import os


MY_EMAIL = os.environ.get("EMAIL_ID")
MY_PASSWORD = os.environ.get("PASSWORD")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key =  os.environ.get("OWN_API_KEY")

weather_params = {
    "lat": -6.175110,
    "lon": 106.865036,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])
will_rain = False
for data in weather_data["list"]:
    condition_data = data["weather"][0]["id"]
    if int(condition_data) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: It's going to rain.\n\nBring your Umbrella."
        )

