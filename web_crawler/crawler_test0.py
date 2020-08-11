from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html>
	<head>
		<title>제목</title>
	</head>
	<body>
		<div><p>문장1</p><p>문장2</p><p>문장3</p></div>
		<div class="animal"> <p>개</p> <p>고양이</p> <p>호랑이</p> </div>
		<div id="name"><p>철수</p><p>영희</p><p>길동</p></div>
		<h1>머리말</h1><p>문장입니다.</p><p>다른 문장입니다.</p>
		<a href="https://wikidocs.net" class="wiki_link" />
	</body>
</html>
"""

# html 변수에 저장된 페이지를 lxml 파서로 파싱하는 코드
bs = BeautifulSoup(html, 'lxml')

# 파싱된 정보에서 첫 번째 p 태그를 보여주는 코드
result = bs.find('p')
print(result)

result = bs.find_all('p')
print(result)

result = bs.find('div', class_='animal')
print(result)

tags = bs.find_all('div', class_='animal')
for tag in tags:
    print(tag.text)

