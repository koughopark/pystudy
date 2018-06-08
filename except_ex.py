def try_f1():
    try:
        lst = [1,3,5,7]
        lst[5]
    except:
        print("Error")

# try_f1()   #IndexError

def try_f2():
    try:
        value = int("10a")
    except ValueError as e:
        print("변환 할 수 없습니다.")
    except Exception as e:
        print("Exception : ", e)
        print("type(e) : ", type(e))

# try_f2()  #ValueError

def try_f3():
    result = 4/0

# try_f3()    #zeroDivisionError

def example():
    num1 = input("첫 번째 숫자를 입력해 주세요 : ")
    num2 = input("두 번째 숫자를 입력해 주세요 : ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 / num2
    except ValueError as e:
        print("정수형이 아니예요")
    except ZeroDivisionError as e:
        print("0으로는 나눌수 없어요")
    except Exception as e:
        print("error.모르겠다 :", e)
    else:   # 오류가 없을 때만 실행
        # print("e : ", e)
        print("{} / {} = {}".format(num1, num2, result))
    finally:    # 오류 여부와 상관 없이 마지막에 실행
        print("예외처리 완료")

# example()

# 특정 경우에는 일부러 예외를 발생시키기도 합니다.
def beware_dog(animal):
    if animal == 'dog':
        # 예외 발생
        raise RuntimeError('멍멍')
    else:
        print("welcom!")

try:
    beware_dog('cow')
    beware_dog('cat')
    beware_dog('dog')
except RuntimeError as e:
    print("e : ", e)
    print("type(e) : ", type(e))