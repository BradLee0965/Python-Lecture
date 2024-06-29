# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요 // 리스트는 [] 로, 튜플은 ()로
# 튜플 자료형(순서O, 중복O, 수정X,삭제X) 한번 용도를 정해놓으면 변하지 않을 때 씀, 기준값

# 선언
a = ()
b = (1,) # 끝을 , 로 찍어야 type이 튜플이 됨
c = (11, 12,13,14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 수정 X
# d[0] = 1500
# print('d - ', d)

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹, 튜플 선언하는것과 마찬가지
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t)
print(t[0])
print(t[-1])

# 언팩킹1 # 묶여있던 패킹을 다시 풀어서 하나의 원소씩 대입 시킴

(x1, x2, x3, x4) = t
print (type(x1),type(x2),type(x3),type(x4))
# 출력확인
print(x1)
print(x2)
print(x3)
print(x4)

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3 # 튜플은 () 없어도 선언됨.
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)


#tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
#list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
#REPL에서 확인해봅니다.
#list와 마찬가지로 다양한 타입이 함께 포함될 수 있습니다.