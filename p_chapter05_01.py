# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수는 일급 함수(일급 객체)이다.
# https://hyeo-noo.tistory.com/283?category=923357
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능

# 함수 객체
def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(6))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(map(var_func, range(1,11)))
print(list(map(var_func, range(1,6))))


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 등
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])
 # % 연산자는 나머지를 반환하는데, 숫자가 2로 나누어 떨어지는 경우 그러니까 나머지가 0인 경우는 자동으로 False로 인식되어 연산 과정에 포함되지 않는 것으로 이해하면 됨

print()
print()

# reduce()
# 시퀀스를 단일 값으로 줄이기 위해 왼쪽에서 오른쪽으로 시퀀스의 항목에 두 인수의 함수를 누적 적용합니다.
# 예를 들어, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])는 다음을 계산합니다.
#  ((((1+2)+3)+4)+5). 이니셜이 있으면 항목 앞에 둡니다.

from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # 누적, 인수를(range) 하나하나 줄여가면서(reduce) 더한다. (add) 
print(sum(range(1,11)))


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))
# 3.14(23) 로 호출 불가능
from inspect import signature
# signature 함수를 통해서 함수의 인자 타입을 알 수 있다.
sg = signature(var_func)

print(sg)
print(sg.parameters)

print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print(five(10))
print(six()) # print(six(50)) --> 호출 안됨. 2개 할당인데 3개 인풋해버림
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))