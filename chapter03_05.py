# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X(순서가 없음), 키 중복X(카테고리 중복x), 수정O, 삭제O)

# 선언, 여러가지 방법이 있음
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None으로 print됨 , get을 많이 씀
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) (__iter)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

# items --> key 와 value를 동시에 가져옴
print('a - ', list(a.items())) 
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print('a - ', a.pop('name'))
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('d - ', d.pop('City'))
# popitem --> 뒤에서 한개의 아이템을 제거함.
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
# 예외
# print('f - ', f.popitem())

print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# 수정
f.update(Age=36)

temp = {'Age': 27}

print('f - ', f)

f.update(temp)

print('f - ', f)
