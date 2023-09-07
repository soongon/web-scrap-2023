PASS_WORD = ''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 원격조정을 할 웹브라우저를 실행
browser = webdriver.Chrome()
# 특정 사이트로 이동
browser.get('https://github.com/login')
time.sleep(5)
# 아이디 입력하고 패스워드를 입력하고 로그인 버튼을 클릭
(browser
    .find_element(By.CSS_SELECTOR, '#login_field')
    .send_keys('soongon', Keys.TAB, PASS_WORD, Keys.ENTER)
 )
time.sleep(10)

# 브라우저 종료
browser.close()