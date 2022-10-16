# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천 , 과거 버전 사용하면 필요하다. 알고 있어야 함. 
# 상대 경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# python 3 부터는 상대경로가 지원되지 않을 예정, 실행하려는 폴더의 위치에 파일 옮겨야 함 

# 예제1
import sub.sub1.module1 #sub 패키지 안의 sub1 패키지 안에 module1 이라는 모듈을 import 한다.
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

# 사용
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2 --> 예제 1 보다 더 간단하게 호출
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # Alias (별명)의 줄임말

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import * # *은 전체를 가져옴. 
from sub.sub2 import *

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()
