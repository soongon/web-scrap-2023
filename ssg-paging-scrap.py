import pprint

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_li_list_from_url(products_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
    }
    res = requests.get(products_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup.select('#ty_thmb_view > ul > li')


def main():

    products_total = []
    for page_num in range(1, 100):
        time.sleep(2)
        li_list = get_li_list_from_url(
            'https://www.ssg.com/service/emart/dvstore/category.ssg?dispCtgId=6000189834&page=' + str(page_num))
        print(len(li_list))
        print(str(page_num) + '페이지 스크래핑 중..')

        if not li_list:
            print(str(page_num) + '페이지 데이터 없음.. 스크래핑 종료..')
            break

        products_page = []
        for li in li_list:
            products_page.append([
                li.select_one('div.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko').text,
                li.select_one('div.cunit_info > div.cunit_price > div > em').text.replace(',', ''),
                (
                    '0' if not li.select_one('div.cunit_info > div.cunit_app > div > span > em')
                    else li.select_one('div.cunit_info > div.cunit_app > div > span > em').text
                ),
                'https:' + li.select_one('div.cunit_prod > div.thmb > a > img.i1')['src'],
            ])
        print(products_page)
        products_total.extend(products_page)

    print(products_total)
    df = pd.DataFrame(products_total)
    df.to_excel('ssg.xlsx')
    print('ok..')


main()
