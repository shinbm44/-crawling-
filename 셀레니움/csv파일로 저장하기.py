from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv

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



# 스크롤 전 높이 

# 자바스크립트 명령어 실패하는 명령어 
# 현재 스크롤의 높이를 알려주는 명령어를 사용 -> 변수 before_h에 담아준다.
before_h = browser.execute_script('return window.scrollY')



# 스크롤 

while True:
    # 맨 아래로 스크롤을 내린다. 
    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
    # 키보드의 END를 눌러준다고 생각하면 된다. 

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(2)

    # 스크롤 후 높이 
    after_h = browser.execute_script('return window.scrollY')

    # 스크롤이 끝에 도달하면 종료   
    if after_h == before_h:
        break

    before_h = after_h

# csv 파일 생성
f = open(r'C:\Users\user\Desktop\크롤링\selenium\셀레니움\data.csv', 'w', encoding ='cp949', newline='')
csvWriter = csv.writer(f)

# 개발자 도구로 찾아보니 와우 상품과 일반 상품의 클래스 선택자 이름이 다르다.  
# 구분해서 처리해줘야함을 발견

# 일반 상품
items = browser.find_elements(By.CSS_SELECTOR, '.product_info_area__xxCTi')
print(len(items))

for item in items:
    # 이름 추출
    name = item.find_element(By.CSS_SELECTOR,'.product_title__Mmw2K').text
    
    # 가격 추출
    # 판매 중지된 상품 처리를 위한 예외처리 
    try:
        price = item.find_element(By.CSS_SELECTOR,'.price_num__S2p_v').text
    except:
        price = '판매중지'

    try:
        link = item.find_element(By.CSS_SELECTOR, '.product_title__Mmw2K > a').get_attribute('href')
    except:
        link = '안잡힘'
    
    print(name, price, link)

    # 데이터 쓰기
    csvWriter.writerow([name, price, link])
    

# 와우 상품
items_wow = browser.find_elements(By.CSS_SELECTOR, '.adProduct_info_area__dTSZf')
print(len(items_wow))




for item in items_wow:
    #이름 추출
    name = item.find_element(By.CSS_SELECTOR,'.adProduct_title__amInq').text
    
    # 가격 추출
    # 판매 중지된 상품 처리를 위한 예외처리 
    try:
        price = item.find_element(By.CSS_SELECTOR,'.price_num__S2p_v').text
    except:
        price = '판매중지'
    
    try:
        link = item.find_element(By.CSS_SELECTOR, '.adProduct_title__amInq > a').get_attribute('href')
    except:
        link = '안잡힘'

    print('wow', name, price, link)

    # 데이터 쓰기
    csvWriter.writerow([name, price, link])


# 파일 닫기 
f.close()

