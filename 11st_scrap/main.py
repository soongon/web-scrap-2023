from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# 페이지 접근
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

# # webdriver 설정(Chrome) - Headless 모드
# chrome_options = Options()
# chrome_options.add_argument("--headless")

url = 'https://www.11st.co.kr/products/2109620962?trTypeCd=STP06'  # 매일유업피크닉

driver = webdriver.Chrome('./chromedriver')
driver.get(url)
time.sleep(2)

# 리뷰 클릭
driver.find_element_by_id('tabMenuDetail2').click()
time.sleep(1)

# 리뷰 iframe 이동
driver.switch_to.frame('ifrmReview')

# 리뷰 더보기를 계속 눌러 모든 리뷰 확보
while True:
    try:
        driver.find_element_by_css_selector('#review-list-page-area > div.area_btn > button').click()
        time.sleep(2)
    except:
        break

time.sleep(1)
page_source = driver.page_source

driver.close()

soup = BeautifulSoup(page_source, 'html.parser')

reviews = []

for ul in soup.select('#review-list-page-area > ul'):
    for li in ul.select('li'):
        stars = 0
        comment = ''
        try:
            stars = int(li.select_one('div > p.grade > span > em').text)
        except:
            continue

        try:
            comment = li.select_one('div > div > div.cont_text_wrap > p').text.strip()
        except:
            pass

        reviews.append([stars, comment])

# 엑셀파일 저장
df = pd.DataFrame(reviews, columns=['별점', '리뷰'])
df.to_excel('11review.xlsx', sheet_name='식품', header=True)
print('job completed')

