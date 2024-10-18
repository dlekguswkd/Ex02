# 모듈

PI = 3.14

# 더하기 함수
def plus(a, b):
    return a + b

# 빼기 함수
def minus(a, b):
    return a - b

# 곱하기 함수
def multi(a, b):
    return a * b

# 나누기 함수
def div(a, b):
    return a / b

# 원의 넓이구하기
def area_circle(r):
    return PI*r**2


# print(plus(55,66))
# print(area_circle(5))

# 직접실행
#print(__name__)       # 언더바 앞뒤로 두개씩 __name__ 이거자체가 변수임
                        # __main__ 이라고 찍음
# 본인이 실행하면 --> __main_
# 남이 부르면 --> 파일명 으로 나옴

# 직접실행  이파일을 실행할때만 실행됨
#    변수         문자열
if __name__ == "__main__":          # 여기서 실행한게 다른곳에서 여기를 import 했을때 실행되는것을 막기위해
                                    # 여기에서만 실행하게하는 if문 
    print("-----")
    print(plus(55,66))
    print(area_circle(5))
