import pprint
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

trs = soup.select('#lst50')

song_list = []

for tr in trs:
    song_list.append([
        int(tr.select_one('td:nth-child(2) > div > span.rank').text),
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
        tr.select_one('td:nth-child(7) > div > div > div > a').text,
    ])
# pprint.pprint(song_list)
df = pd.DataFrame(song_list)
df.to_excel('melon_1_50.xlsx', index=False, header=['순위', '제목', '아티스트', '앨범명'])

print('job completed..')
