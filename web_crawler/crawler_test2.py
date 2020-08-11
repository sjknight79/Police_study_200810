import requests
from bs4 import BeautifulSoup

# 이미지 처리를 위해 사용되는 라이브러리
from io import BytesIO
from PIL import Image

# get 방식으로 서버에 해당 주소의 페이지 요청
url = "https://wikidocs.net"
page = requests.get(url)
# print(page.text)

# 해당 페이지의 html 내용들(page, content)을 lxml 파서로 파싱합니다.
bs = BeautifulSoup(page.content, 'lxml')

# a 태그들 중 클래스가 book-subject인 것들을 따로 저장합니다.
img_sources = bs.find_all('img', class_='book-image')
print(img_sources)

img_links = []
for img_source in img_sources:
    img_link = url + img_source.attrs['src']
    img_links.append(img_link)
print(img_links)

# 이미지를 출력하기 위해 사용하는 라이브러리
import matplotlib.pyplot as plt
for img_link in img_links:
    res = requests.get(img_link)
    img = Image.open(BytesIO(res.content))

    plt.axis('off')
    plt.imshow(img)
    plt.show()


