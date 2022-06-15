from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://accounts.google.com/')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#identifierId')\
    .send_keys('ksoongon97', Keys.ENTER)
time.sleep(2)
ActionChains(driver).send_keys('1q2w3e4r##').pause(1).key_down(Keys.ENTER).perform()
time.sleep(2)
driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#\:3i > div > div').click()

ActionChains(driver)\
    .send_keys('ksoongon97@gmail.com')\
    .key_down(Keys.TAB)\
    .key_down(Keys.TAB)\
    .pause(0.5)\
    .send_keys('hello')\
    .key_down(Keys.TAB)\
    .send_keys('hello')\
    .key_down(Keys.TAB)\
    .pause(1)\
    .key_down(Keys.ENTER)\
    .perform()
time.sleep(5)
driver.close()
