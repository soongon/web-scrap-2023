import time

from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

# 헤더 변조
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# html 확보
#res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

# html 확보 --> 셀레니움으로 한다.
browser = webdriver.Chrome()
browser.get('https://www.melon.com/chart/index.htm')
time.sleep(3)
html_source = browser.page_source

soup = BeautifulSoup(html_source, 'html.parser')

# 분석후 필요한 데이터 파싱
#tr_tags = soup.select('#frm > div > table > tbody > tr')

melon_list = []
for tr in soup.select('#frm > div > table > tbody > tr'):
    melon_list.append([
        tr.select_one('td:nth-child(2) > div > span.rank').text,
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
        int(tr.select_one('td:nth-child(8) > div > button > span.cnt')
            .text.replace(' ', '')
            .replace('\n', ''
            .replace('\t', ''))
            .strip()[3:].replace(',', '')),
        #tr.select_one('td:nth-child(4) > div > a > img')['src'],
    ])

# import pandas as pd
# list of list 확보..
# 저장.. CSV, Excel, DB-table
df = pd.DataFrame(melon_list)
#print(df)
df.to_csv('melon.csv', index=False)
df.to_excel('melon.xlsx', index=False)
print('csv file export ok..')
# 14:55

browser.close()