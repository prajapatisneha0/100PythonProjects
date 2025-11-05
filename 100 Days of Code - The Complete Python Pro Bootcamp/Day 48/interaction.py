from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Navigate to wikipedia
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org")
article_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(article_count.text)
# article_count.click()

# Find "search" <input> to selenium
search = driver.find_element(By.NAME,value="search")
search.send_keys("Python",Keys.ENTER)