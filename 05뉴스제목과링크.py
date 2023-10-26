import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_txt = input('크롤링할 키워드는 무엇입니까?')

responese = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
html = responese.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') # 결과는 리스트

for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져온다
    url = link.attrs['href'] # href의 속성값을 가져온다

    print(title, url)