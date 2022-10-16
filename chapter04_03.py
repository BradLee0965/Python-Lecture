# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr,expression>: 
#    <statement(s),code>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1
    
# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# if 중첩
# 예제3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')  
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')   

# 예제5
i = 1

while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1


# While - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:# break 때문에 else 실행 안됨.
    print('else out.')

# 예제7 
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else: 
    print(s, 'not found in list.')
    
    
# 무한반복
# while True:
#     print('Foo')

# 예제8 #이해 안됨 --> a가 True가 아닐때 즉, false 일때 (a.pop 끝나고 난 이후에 아무것도 없어짐. 즉 false 됨) break.
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())








