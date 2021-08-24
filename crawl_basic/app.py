# 파이썬 크롤러 기본 + 저장하는법


import requests  #파이썬으로 웹사이트 접속을 도와주는
from bs4 import BeautifulSoup # 파이썬으로 HTML 웹문서 분석 도와주는
def 작명(i):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={i}')

    soup = BeautifulSoup(데이터.content,'html.parser')

    print(soup.find_all('strong',id="_nowVal")[0].text)
    print(soup.find_all('span',class_="tah")[5].text)
    

작명('003490')

f = open('a.txt','w')
f.write('aaa')
f.close()

# print(soup.select('.gray .f_down em').text())

# 이미지 = soup.select('#img_chart_area')[0]

# print(이미지['src'])



