import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

url = "https://wikidocs.net"
page = requests.get(url)
bs = BeautifulSoup(page.content, 'lxml')

# 띄어쓰기는 .으로 처리해주면 됨  a태그의 “btn btn-default.btn-xs” 클래스
recommendations = bs.select("a.btn.btn-default.btn-xs > strong")

rec_num_list = []

for number in recommendations:
	temp = number.text
	# 숫자에 있는 콤마(,) 없애는 코드
	rec_num = int(temp.replace(',', ''))
	rec_num_list.append(rec_num)

print(rec_num_list)
