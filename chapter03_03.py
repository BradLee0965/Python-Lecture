# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱 --> 원하는 데이터를 꺼내오는 과정 
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1]) # 숫자끼리 더하는거 가능함, 문자끼리 가능함 d[2] + d[3]
print('d - ', d[-1])
print('e - ', e[-1][1]) # -1은 오른쪽 첫번째 위치 나타내는것, 1은 그 리스트에서 1번 자리위치 가리킴
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d) # 각자 위치에서 더해지는게 아닌 list--list 연결 됨
print('c * 3 - ', c * 3) # 3번 연달아서 나옴.
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0])) # str 씌워서 문자열로 변환

# 값 비교
print(c == c[:3] + c[3:])

# 같은 id 값
temp = c
print(c == temp)


# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4 # c의 첫번째 데이터를 4로 대체
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] 하면 list 안에 list가 들어감 c[1:2]--> 1번 위치 부터 (2-1)개 변환
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6) # 오른쪽 맨 끝자리에 데이터 삽입
print('a - ', a)
a.sort() # 오름 차순으로 출력하는것
print('a - ', a)
a.reverse() # 역순으로 출력
print('a - ', a)
print('a - ', a.index(5)) # 인덱스 번호에 있는 함수 호출
a.insert(2, 7) # 두번째 위치에 7을 넣는것, 대체가 아니고 삽입 되는것 
print('a - ', a)
a.reverse()
a.remove(1) #delete 는 그 위치에서 삭제, remove는 특정 값 삭제
print('a - ', a)
print('a - ', a.pop()) # 마지막 인덱스 원소를 가져오고 리스트에서 그 원소를 제거한후 출력함.
print('a - ', a.pop()) # last in, first out 이라고 하기도 함. 
print('a - ', a)
print('a - ', a.count(4)) # 4의 갯수 출력  
ex = [8, 9]
a.extend(ex) # 끝에다 붙임
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)