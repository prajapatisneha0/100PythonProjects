from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))


event_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}
for n in range(len(event_time)):
    events[n] = {
        "time":event_time[n].text,
        "name":event_name[n].text,
    }
print(events)

driver.close()
