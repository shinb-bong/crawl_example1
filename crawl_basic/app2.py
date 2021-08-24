# 무한스크롤 사이트 크롤링

import requests
import json
import time
data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')
# print(data.content)

딕셔너리 = json.loads(data.content) # 파이썬으로 딕셔너리로 바꿔야 편하게 조작가능
print(딕셔너리['data'][0]['Close'])
print(딕셔너리['data'][0]['DT'])
시간 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1620511200000/1000))
print(시간)


########### time ########

print(time.time())
