#Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# non -blocking 비동기 처리
# Blocking I/O : 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기
# non-blocking I/O : 호출된 함수가(서브루틴) return 후 호출한 함수 (메인루틴) 제어권 전달 -> 타 함수는 일 지속
# 쓰레드 단점 : 디버깅, 자원 접근 시 레이스 컨디션(경쟁 상태) , 데드락(Dead lock) -> 고 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 x -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현되어있어야 하거나, 직접 비동기로 )

# Asyncio 웹 스크래핑 실습
# Beautiful Soup 추가
# 스케쥴러 사용시 주기적으로 데이터 수집 가능
# 수집 정보 DB 저장 -> 파이썬 기초 강의 참고

import asyncio
from bs4 import BeautifulSoup
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://www.inflearn.com/']

async def fetch(url, executor) :
    print('Thread Name : ', threading.current_thread().getName(), 'start', url)
    res = await loop.run_in_executor(executor, urlopen, url)    
    soup = BeautifulSoup(res.read(), 'html.parser')
    # print(soup.prettify())
    result_data = soup.title 
    print('Thread Name : ', threading.current_thread().getName(), 'done', url)
    return result_data

async def main() : 
    executor = ThreadPoolExecutor(max_workers=10)
    
    futures = [
        asyncio.ensure_future(fetch(url,executor)) for url in urls
    ]
    rst = await asyncio.gather(*futures)
    print()
    print('Result : ', rst)
 
    
if __name__ == '__main__' :
    loop = asyncio.get_event_loop()
#    print(loop)
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start
    print('Total Running Time : ', duration)

