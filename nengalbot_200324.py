# -*- coding: utf-8 -*- 

import request

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from datetime import datetime

from urllib.request import urlopen

from bs4 import BeautifulSoup

import pyperclip

import time



# 0. 크롤링



_contents = '사진을 누르면 예약페이지로 이동한다요~☆'

_title = '[개인 테스트용]굿스마 {}월 {}일 예약 목록 안내'.format(datetime.today().month,datetime.today().day)

print(_title)

html = urlopen("https://www.goodsmile.info/en/onlinedates")

bsObject = BeautifulSoup(html, "html.parser")

detailed = bsObject.find_all('div',{'id':'detailedview'})

all = detailed[0].find_all(True,{'class':['syukkagreen','nendoroid','nendoroiddoll','playset']})

for link in all:
    try :
        if (str(link).find('search') != -1):
            continue
        _contents = _contents + str(link)
        link = link.find('a')
        start = str(link).find('href=\"')
        end = str(link).find('\" target')
        print(str(link)[start+6:end])
        newpage = urlopen(str(link)[start+6:end])
        obj = BeautifulSoup(newpage, "html.parser")
        price = obj.find_all(True,{'class':['qty-right']})
        _contents = _contents + str(price[1])
    except ValueError :
        pass


id = 

pw = 



URL = 'https://www.dcinside.com'

GALL = 'https://gall.dcinside.com/mgallery/board/write/?id=nendoroid'



TITLE = _title

pyperclip.copy(_contents)



chrome_options = webdriver.ChromeOptions()

##chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')

##chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")



# 1. 드라이버 로드

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)

driver.implicitly_wait(3)





# 2. DC inside 접속

driver.get(URL)

time.sleep(3)



# 3. 로그인

driver.find_element_by_name('user_id').send_keys(id)

driver.find_element_by_name('pw').send_keys(pw)

driver.find_element_by_id('login_ok').click()



# 4. 갤러리 글쓰기 페이지 이동

driver.get(GALL)

time.sleep(3)



# 5. 제목 & 내용 입력

driver.find_element_by_name('subject').send_keys(TITLE)

driver.find_element_by_id("tx_switchertoggle").click()

time.sleep(1)
driver.find_element_by_id("tx_canvas_source").send_keys(Keys.CONTROL, 'v')


# 6. 저장

time.sleep(3)

driver.find_element_by_xpath("//button[@type='image'][@class='btn_blue btn_svc write']").click()

time.sleep(1)



# 7. 드라이버 종료

driver.quit()


