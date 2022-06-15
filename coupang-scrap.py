import pprint

import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get('https://www.ssg.com/service/emart/dvstore/category.ssg?dispCtgId=6000189834')
soup = BeautifulSoup(res.text, 'lxml')

li_list = soup.select('#ty_thmb_view > ul > li')

products = []
for li in li_list:
    likes = ''
    try:
        likes = li.select_one('div.cunit_info > div.cunit_app > div > span > em').text
    except:
        likes = '0'

    products.append([
        li.select_one('div.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko').text,
        li.select_one('div.cunit_info > div.cunit_price > div > em').text.replace(',', ''),
        likes,
        'https:' + li.select_one('div.cunit_prod > div.thmb > a > img.i1')['src'],
    ])
print(products)
# df = pd.DataFrame(products)
# df.to_excel('ssg.xlsx')
# print('ok..')
