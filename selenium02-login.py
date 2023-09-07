
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser 확보
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
options.add_argument("Accept-Language=ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3")

browser = webdriver.Chrome(options=options)
# 로그인 페이지로 이동
browser.get('https://estudy.kitri.re.kr/usrs/userManage/usrLoginForm.do')
time.sleep(3)
# 로그인 수행
(browser
    .find_element(By.ID, 'p_usrid')
    .send_keys('soongon', Keys.TAB, '1q2w3e4r!', Keys.ENTER))
time.sleep(3)
# 사용자 홈페이지로 이동
browser.get('https://estudy.kitri.re.kr/usrs/mypage/myHome.do')
time.sleep(2)
# 스크래핑할 페이지(사용자 홈페이지)의 소스를 가져옵니다.
html_source = browser.page_source
# html을 beautifulsoup을 사용해서 파싱 가능하게 만든다.
soup = BeautifulSoup(html_source, 'html.parser')

browser.close()
