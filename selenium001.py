from selenium import webdriver
import time

from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb')
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
print(soup)
driver.close()


tags = soup.select('#slot-15 > div > div > div.GridContainer-module__gridMainContainer_24aSWvAi-VAzH5okoDOqpb > div.a-row.Grid-module__gridSection_1SEJTeTsU88s6aVeuuekAp > div > div')
print(len(tags))
