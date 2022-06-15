
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://accounts.google.com/')
time.sleep(2)

id_input_box = driver.find_element(by=By.CSS_SELECTOR, value='#identifierId')
id_input_box.send_keys('ksoongon97')
time.sleep(1)
driver\
    .find_element(by=By.CSS_SELECTOR, value='#identifierNext > div > button')\
    .click()
time.sleep(1)
driver\
    .find_element(by=By.CSS_SELECTOR, value='#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')\
    .send_keys('1q2w3e4r##', Keys.ENTER)
time.sleep(2)
html = driver.page_source
print(html)
driver.close()
