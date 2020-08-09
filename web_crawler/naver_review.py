import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=188909"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())

ul = soup.find("ul", class_="rvw_list_area")
# print(ul)
lis = ul.find_all("li")

for i, li in enumerate(lis):
    print(i, "="*50)
    print(li.a.text)
    print(li.span.em.text)

