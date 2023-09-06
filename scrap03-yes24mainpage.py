import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.yes24.com/main/default.aspx')
soup = BeautifulSoup(res.content, 'html.parser')

books_root = soup.select_one('#yWelMid > div.yWelNowBook > div.nowBookArea')

# 세개의 자식 div 를 가지고 온다.
book_divs = books_root.select('div.nowBookSet') # 세개의 자식 div를 리스트로 반환

books = []
for book_div in book_divs:
    for book_li in book_div.select('ul > li'):
        books.append([
            book_li.select_one('div > p.goods_name > a').text,
            book_li.select_one('div > p.goods_pubGrp > span.goods_auth').text,
            book_li.select_one('div > p.goods_price > em').text
        ])

print(books)