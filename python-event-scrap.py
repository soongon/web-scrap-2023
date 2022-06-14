import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 해당 URL을 통해 HTML 전달 받기
res = requests.get('https://www.python.org/events/')
# 2. 응답이 정상적인 것이 확인되면 BeautifulSoup 을 통해서 parsable 형태로 변환
soup = BeautifulSoup(res.text, 'html.parser')
# 3. 실제 컨텐츠 확보 (첫번째 이벤트의 날짜, 이벤트명, 타입 --> 3가지 데이터 확보 --> list 표현)
event_date = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > p > time').text
event_name = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > h3 > a').text
event_type = soup.select_one('#content > div > section > div > div > ul > li:nth-child(1) > p > span').text

a_event = [event_date, event_name, event_type]

# 4. 리스트를 엑셀로 변환 --> pandas 라이브러리를 사용
df = pd.DataFrame(a_event)
df.to_excel('python-event.xlsx')
print('엑셀로 잘 저장되었습니다.')
