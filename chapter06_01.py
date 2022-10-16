# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수 # 누가 무슨 일을 할 것인가에 초점
# 절차 지향 프로그래밍 : 어떤 절차로 할 것인가? 에 초점
# 객체 : 소프트웨어에서 우리가 구현할 대상. 
# 클래스 and 인스턴스 차이 이해, 클래스는 붕어빵 틀, 인스턴스는 클래스를 가지고 코드에 사용하는 객체 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # object 상속
    # 클래스 속성, 같은 클래스면 클래스 속성은 같다. 똑같은 붕어빵 틀
    species = 'firstdog'
    
    # 초기화/인스턴스 속성 #다른 붕어빵 재료
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2) # a 는 class 'Dog'의 인스턴스다.
b = Dog("baby", 3)
c = Dog("mikky", 2)
# 비교
print(a == b, id(a), id(b))
print(id(a),id(c)) # id 값 다름, 인스턴스화 한 것들은 똑같은 인스턴스가 들어가도 다른 객체로 간주함. 
# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)    
    
# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog': # 직접 접근 가능
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest: # __init__이 없음. 기본적으로 넣어줄 것이 없어서, 파이썬이 알아서 공백으로 놔둠. 
    def func1(): # 암묵적으로 매개변수가 없는 메소드는 class 메소드다. 
        print('Func1 called')
    def func2(self): # self 는 인스턴스를 요구한다. 즉 인스턴스 메소드다.
        print(id(self))
        print('Func2 called')


f = SelfTest() #클래스를 f로인스턴스화 시킴, self 는 인스턴스를 요구함.
### 설명 
# 매개변수 없는것 --> 클래스로 직접 접근해서 호출해야함. SelfTest.func1()
# 매개변수 self로 선언한 것 --> 클래스를 인스턴스화 시켜서 호출 해야함. f =SelfTest(), f.func2()

print(dir(f)) # 안의 메소드 확인 
print(id(f)) # id(f) 값과 id(self)값이 동일
# f.func1() # 예외
f.func2()
SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 
    stock_num = 0 # 재고
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self): #__del__ -> 객체가 소멸할때 자동으로 호출되는 메소드
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__) # 인스턴스의 네임스페이스에 없으면 클래스 네임스페이스에서 찾는다. 
print(user2.__dict__) 
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num) # class 메소드는 모두 공유하기때문에 1이 아닌 2가 나온다

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
        
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound) #sound 변수는 변수 선언할때
    #('a =Dog('lee','3')) 선언하지 않고 speak 메소드를 부를때 선언하기때문에 self가 붙지 않는다 (??)
    # 처음에 변수 인스턴스 선언시, sound 입력 안해도 됨. 못함.


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))