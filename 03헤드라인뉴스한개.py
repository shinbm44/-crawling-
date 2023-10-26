import requests
from bs4 import BeautifulSoup


header = {'User-agent' : 'Mozila/2.0'}

response = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100', headers = header)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.select_one('.sh_text')

print(title.text.strip())
