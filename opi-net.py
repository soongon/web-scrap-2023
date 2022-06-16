from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')

    driver = webdriver.Chrome('./chromedriver', options=options)

    driver.get('http://www.opinet.co.kr/searRgSelect.do')
    driver.get('http://www.opinet.co.kr/searRgSelect.do')
    # 서울 -> 강남구를 선택한다.
    driver.implicitly_wait(3)
    select_sido = Select(driver.find_element_by_name('SIDO_NM0'))
    select_sigungu = Select(driver.find_element_by_name('SIGUNGU_NM0'))

    price_list_total = []

    for sido_index in range(1, len(select_sido.options)):
            select_sido = Select(driver.find_element_by_id('SIDO_NM0'))
            select_sigungu = Select(driver.find_element_by_id('SIGUNGU_NM0'))
            select_sido.select_by_index(sido_index)
            time.sleep(1)
            for sigungu_index in range(1, len(select_sigungu.options)):
                select_sigungu = Select(driver.find_element_by_id('SIGUNGU_NM0'))
                select_sigungu.select_by_index(sigungu_index)
                time.sleep(1)

                price_list_total.extend(scrap_oil_price(driver.page_source))

    driver.close()
    print(price_list_total)


def scrap_oil_price(source):
    soup = BeautifulSoup(source, 'html.parser')

    oil_price_list = []
    for tr in soup.select('#body1 > tr'):
        station_name = 'no name'
        gasoline = 0
        diesel = 0
        try:
            station_name = tr.find('td', {'class': 'rlist'}).find('a')['href'].split(',')[-14][1:-1]
        except:
            pass

        try:
            gasoline = tr.find_all('td', {'class': 'price'})[0].text.strip()
        except:
            pass

        try:
            diesel = tr.find_all('td', {'class': 'price'})[1].find('font').text.strip()
        except:
            pass

        oil_price = [station_name, gasoline, diesel]
        print(oil_price)
        oil_price_list.append(oil_price)

    return oil_price_list

main()