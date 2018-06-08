# format_ex.py
# 문자열 서식

# 서식 문자
'''
%s : 문자열
%d : 정수
%f : 부동소수
%% : % 리터럴
'''

format = "I have %d apples"
print(format % 10)  # I have 10 apples

print("Interest Rate is %.2f%%" % 1.24)

# 두 개 이상의 값을 넣고 싶을 때
format = "total: %d개, get: %d개"
print(format % (10, 3))

# format과 값의 형식이 일치하지 않으면 TypeError 발생


# 고급 포맷팅
format_str = "I have {} apples, and I ate {} apples."
print(format_str.format(5,3))


# 서식에 설정되 ㄴ공간의 개수와 실제 값의 개수가 다르면 IndexError 발생
print(format_str.format(10,3,1))
# print(format_str.format(10))      # 많으면 되고 적으면 안됨


# 이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format(total = 10, num = 3))
# print(format_str.format(total=10))      # KeyError

# dict 객체를 이용한 포맷
print(format_str.format_map({"total":5, "num":2}))









