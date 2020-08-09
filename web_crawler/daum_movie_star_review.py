import requests
from bs4 import BeautifulSoup as bs

url = "https://movie.daum.net/moviedb/grade?movieId=134698&type=netizen"

import csv
csv_file = open("./강철비2_daum.csv", 'w', newline='')
# csv_file = open("./강철비2_다음.csv", 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file) # writer를 통해서 파일 작성
row = ['평점', '리뷰']
csv_writer.writerow(row)


# for x in range(1, int(count)//10 + 1):
for x in range(1, 4):
    print(x, "="*50)
    html = bs(requests.get(url + "&page=" + str(x) ).content, "lxml", from_encoding="utf-8")
    # print(html)
    ul = html.find("ul", class_="list_review list_netizen")
    # ul = dl.find("ul")
    li = ul.find_all("li")
    for a in li:
        score = a.find("div", class_="raking_grade").em.text
        review = a.find("p", class_="desc_review").text.strip()
        print("평점 :", score)
        print("리뷰 :", review)

        row = [score, review]
        if review != "":
            try:
                csv_writer.writerow(row)
            except:
                continue

csv_file.close()

print("=" * 50)
print("데이터가 저장 되었습니다.")
print("=" * 50)


