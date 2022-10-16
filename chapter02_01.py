# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력
print('Python Start!') 
print("Python Start!") 
print("""Python Start!""")
print('''Python Start!''')

print()

# separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션 사용, Learn Python으로 파일 이름을 쓰겠다고 선언.
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f)
# d(integer)는 정수, s(string)는 문자열, f(float)는 실수
# %는 연결해주는 다리, 즉 첫번째 s는 one을 대체

print('%s %s' % ('one', 'two')) #여기는 문자열로 선언했기때문에 다른것들은 못옴.
print('{} {}'.format('one', 'two')) #선언 하지 않았기 때문에 d s f 다 올수 있음.
print('{1} {0}'.format('one', 'two')) # 인덱스는 0 부터 시작, 순서 지정한것.

# %s
print('%10s' % ('nice',)) #10은 총 자릿수를 의미함. 
print('{:>10}'.format('nice')) #위의 결과값과 동일, 다만 코딩형식이 다름.

print('%-10s' % ('nice',)) # -는 왼쪽부터 채우는것
print('{:10}'.format('nice'))

print('{:d<10}'.format('nice')) # niceddddd
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('pythonstudy',)) # .으로 단어 절삭, 즉 pytho 까지만 출력
print('{:.5}'.format('pythonstudy')) #동일한 출력
print('{:10.5}'.format('pythonstudy')) #동일한 출력

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,)) # 총 자릿수 6자리 정수부 빈칸은 0으로 채운다., 소수부 2자리 출력
print('{:06.2f}'.format(3.141592653589793))