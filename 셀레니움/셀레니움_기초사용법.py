from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options= chrome_options)


# 브라우저 생성
browser = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 웹 사이트 열기 
browser.get('https://shopping.naver.com/home')

# 브라우저가 아직 안 열렸는데 버튼 누름이 실행되면 원하는 바로
# 안 움직일 수 있다.. -> 10초 기다려(로딩이 끝날 때까지 10초는 기다려줌)
browser.implicitly_wait(10)


# 검색창 클릭
search = browser.find_element(By.XPATH ,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
# 엔터치기
search.send_keys(Keys.ENTER)