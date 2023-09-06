import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_product_list_with_soup(soup):
    product_list = []
    for li_tag in soup.select('#productList > li'):
        img_url = li_tag.select_one('a > dl > dt > img')['src']
        img_filename = img_url[img_url.rindex('/') + 1:]

        download_image(img_url, img_filename)

        product_list.append([
            li_tag.select_one('a > dl > dd > div.name').text.strip(),
            int(li_tag.select_one('a > dl > dd > div.price-area > div > div.price > em > strong')
                .text.replace(',', '')),
            img_filename,
            int(li_tag.select_one('a > dl > dd > div.other-info > div > span.rating-total-count')
                .text[1:-1])
        ])

    return product_list


def download_image(img_url, img_filename):
    res_image = requests.get('https:' + img_url)
    with open('./images/' + img_filename, 'wb') as file:
        file.write(res_image.content)
        # print(img_filename, ' 저장되었습니다.')


def save_file(products):
    df = pd.DataFrame(products)
    df.to_csv('coupang_products.csv', index=False)


def main():
    # 헤더 변조
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    # html 확보
    product_list = []
    for page in range(1, 18):
        res = requests.get('https://www.coupang.com/np/campaigns/82/components/115574?page='
                           + str(page), headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')
        # soup 객체 줄께 product_list 반환해줘
        product_list_page = get_product_list_with_soup(soup)
        product_list.extend(product_list_page)
        print(page, ' 페이지 스크래핑 완료')

    save_file(product_list)
    print('job completed..')


main()
