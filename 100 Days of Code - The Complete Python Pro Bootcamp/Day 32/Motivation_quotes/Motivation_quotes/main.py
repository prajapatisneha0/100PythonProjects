import smtplib
import datetime as dt
import random
import os

MY_EMAIL = os.environ.get("EMAIL_ID")
MY_PASSWORD = os.environ.get("PASSWORD")

now= dt.datetime.now()
weekday =now.weekday()
print(weekday)
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL ,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )