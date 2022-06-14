import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.python.org/events/')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a')

print(the_tag.text)

