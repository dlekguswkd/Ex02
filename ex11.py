# 스코핑 룰(Scope) 함수

x=5                     # global 글로벌 (밖에 선언된) 전역
def calPlus(no):
    return no+x

print(calPlus(10))      # 10+5
print("----------------")


def calPlus2(no):
    x=1                 # local 로컬 (함수안에 선언된)
    return no+x

print(calPlus2(10)) 
print("----------------")


# 블록 스코프  -> 함수 스코프  (함수안이면 어디서 생겨도 함수에서는 살아있음) 함수밖에서는 죽음
def calPlus3(mode, no):

    if mode == 1:
        sum = no + 1
    elif mode == 2:
        sum = no + 2
    else:
        print("에러")

    return sum

print(calPlus3(10)) 

