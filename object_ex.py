# object_ex.py

print(id(3))

# 변수에 3을 담는다
# 3 객체를 만들고
# 변수에 3객체의 ID를 연결 심볼 테이블에 저장 # id() 주소값을 리턴

a = 3
# a의 id 값을 확인해 봅시다.
print("id(a) : ", id(a))

b = 3
print("id(b) : ", id(b))

b = 4
print("id(b) : ", id(b))


# 객체 심볼 테이블

# 글로벌 영역
g_a = 2018
g_b = "symbol"

# 로컬 영역 변수 확인을 위한 함수
def f():
    l_a = "local"
    l_b = 5
    # 로컬 스코프의 심볼 테이블
    print(locals())

print("--------------- Local --")
f()

print("-------------- Global --")
print(globals())

print("f" in globals().keys())

# 객체 복사
print("-------------- object Copy --")
x = [1,2,3]
# 레퍼런스 복사
y = x
print(x == y)
print(hex(id(x)), hex(id(y)))

x[1] = 4
print(y[1])

# 복제의 시도:1
y = x[:]
print("x : ", x)
print("y : ", y)

x[1] = 0
print(y[1])

# 복제의 시도: copy 모듈의 활용
import copy

y = copy.copy(x)
print(x is y)   # ==
print("x : ", x)
print("y : ", y)
x[1] = 100
print("x[1] = 100 -> ")
print("x : ", x)
print("y : ", y)


print("---------------------------------------")

# 깊은 복제
a = [1,2,3]
b = [4,5,a]
x = [a,b,100]

print("a : ", a)
print("b : ", b)
print("x : ", x)

y = copy.copy(x)
print("y : ", y)

a[1] = 0
print("a : ", a)
print("b : ", b)
print("x : ", x)
print("y : ", y)

# Deep Copy
y = copy.deepcopy(x)
print("y : ", y)

a[1] = 100

print("x : ", x)
print("y : ", y)    # 연관을 주지 않는다.

# deepcopy는 객체를 다룰때 아주 중요하다.
