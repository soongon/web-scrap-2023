import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

a_song = [
    int(soup.select_one('#lst50 > td:nth-child(2) > div > span.rank').text),
    soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
    soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
    soup.select_one('#lst50 > td:nth-child(7) > div > div > div > a').text,
]

pd.DataFrame(a_song).to_excel('melon.xlsx')
print('ok...')
