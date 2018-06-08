# #print 함수 안에 출력할 내용을 인자값으로 전달.
print(2018)
print(3.141592)
print("hello world")

#여러 내용의 연속 출력 : ,로 연결
print("Hello", "world")

#문자열을 합쳐 출력할 때 : +로 연결
print("hello" + " " + "world")

#문자열 반복 출력 : * 갯수
print("Python" * 3 )

print()

#문자열과 다른 형식을 + 했을 경우 : TypeError
#print(3 + "Python")

# Solution : 형 변환을 실행함
print(str(3) + "python")

#구분자 sep, end 변경
print("박경호", "박태준", "도영석", sep=":", end="")
print("추가 문자열 ㅋ")