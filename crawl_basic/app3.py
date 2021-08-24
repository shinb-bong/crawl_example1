# 파이썬 멀티 쓰레딩 프로세싱

from bs4.element import ResultSet
import requests
import json
import time

url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def 크롤러함수(구멍):
  data = requests.get(구멍)
  딕셔너리 = json.loads(data.content)
  return 딕셔너리['data'][0]['Close']

# 멀티쓰레딩으로 코드 실행시키는 법
from multiprocessing.dummy import Pool as ThreadPool

result = []
pool = ThreadPool(4)
result = pool.map(크롤러함수,url)
print(result)
pool.close()
pool.join()

# map 함수란?
# 함수를 리스트에 다적용해달라~
# map(아무거나함수명, 리스트자료)



