
# 네트워크 통신을 위해 requests 모듈을 사용
import requests
from bs4 import BeautifulSoup

# get 방식으로 서버에 해당 주소의 페이지 요청
url = "https://wikidocs.net"
page = requests.get(url)
# print(page.text)

# 해당 페이지의 html 내용들(page, content)을 lxml 파서로 파싱합니다.
bs = BeautifulSoup(page.content, 'lxml')

# a 태그들 중 클래스가 book-subject인 것들을 따로 저장합니다.
book_list = bs.find_all('a', class_='book-subject')

print(book_list)

links = []
titles = []

for a in book_list:
    # print(a)
    # print(a.attrs)
    link = url + a.attrs['href']
    links.append(link)

    title = a.text
    titles.append(title)

    # 링크와 제목 순서대로 출력
    print(link, title)

