# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드  r, 쓰기모드 w, 추가 모드 a(append), 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1

f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # 'r' 또는 'rt' t는 기본값
f = open('./course/example/resource/it_news.txt', 'r', encoding='UTF-8') # vs code 로 실행시 vs code 있는 위치에서 상대경로 실행. 
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f: # with 쓰면 close 함수 안써도 됨.
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기 , read(10) : 10Byte

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20) # 커서가 있어서 내가 마지막으로 읽은 위치를 기억하고 있음. 
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

# 예제4
# readline : 한 줄 씩 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
        
print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f: # 'a' 쓰면 기존 있는거에서 추가 됨.
    f.write('I love python2\n')
    
    
# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
    
# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f) # file 옵션 넣으면, 해당 파일에 내용 기입되고 print는 되지 않는다. 
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)