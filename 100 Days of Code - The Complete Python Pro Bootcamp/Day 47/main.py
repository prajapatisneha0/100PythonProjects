from bs4 import BeautifulSoup
import requests
import smtplib
import os
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url,headers=header)

soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price

price = soup.find(class_="a-offscreen").getText()
# print(price)
price_without_currency = price.split("$")[1]
# print(without_currency)
price_as_float = float(price_without_currency)
# print(price_as_float)

MY_EMAIL = os.environ.get("EMAIL_ID")
MY_PASSWORD = os.environ.get("PASSWORD")

# Get the product title

title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the email ===========================

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
