import requests
import smtplib
from email.message import EmailMessage
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

MY_EMAIL = os.environ.get("EMAIL_ID")
MY_PASSWORD = os.environ.get("PASSWORD")



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

# yesterday_data = data_list[0]
yesterday_closing_price = data_list[0]["4. close"]
print(yesterday_closing_price)


    #Get the day before yesterday's closing stock price

# day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = data_list[1]["4. close"]
print(day_before_yesterday_closing_price)

    #Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference_of_price = float(yesterday_closing_price)- float(day_before_yesterday_closing_price)
print(difference_of_price)
up_down = None
if difference_of_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

    #Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percentage = round(difference_of_price/ float(yesterday_closing_price) * 100 , 2)
print(diff_percentage)

    #If TODO4 percentage is greater than 5 then print("Get News").
    #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percentage > 5 :
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python

    #Create a new list of the first 3 articles headline and description using list comprehension.
    # to send a separate message with each article's title and description to your phone number.

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline:{articles['title']} .\nBrief:{articles['description']}"
        for articles in  three_articles
    ]

#TODO 9. - Send each article as a separate message via Email.

    for article in formatted_articles:
        msg = EmailMessage()
        msg["Subject"] = f"Stock Alert - {STOCK_NAME}"
        msg["From"] = MY_EMAIL
        msg["To"] = MY_EMAIL
        msg.set_content(article)

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.send_message(msg)

    print("email sent!")
else:
    print(f"No major stock change. Change was {diff_percentage}%. No email sent.")



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
