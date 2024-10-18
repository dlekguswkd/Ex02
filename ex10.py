# 함수정의  def
# 정의는 위에다가 해야함 -> 다 위에 올려다놓음

"""
java
public int plus (a, b) {
    sum = a +b;
    return sum;
}

js
function plus(a,b) {
    sum = a +b;
    return sum;
}

익명함수
let plus = function () {
    sum = a +b;
    return sum;
}

기명함수
let plus = () => {
    sum = a +b;
    return sum;
}
"""

# 정의
def plus(a, b):
    sum = a + b
    return sum

# 실행(사용)
result = plus(5,3)
print(result)


# 문자열 더하기 숫자는 불가능
# result = plus(5, "한글")          숫자 + 문자열 x
# print(result)

print("---------------------")
# 정의  -> 리턴값 없는경우
def my_function():
    print("hello function")
# 실행
my_function()


# 정의   -> 내용이 없는경우
def none_function():
    pass    # 아무것도 적을게 없을때 안쓰면 오류뜨기때문에 대신 이걸 써줌

# 사용
none_function()

print(type(none_function))          # <class 'function'>


print("---------------------")
result = 8, 15      # 튜플 읽기전용리스트   -> 패킹기술
print(result)

# 패킹기술을 이용한 함수정의    -> 두개의 리턴값
def sum_and_mul(a,b):
    sum = a + b
    mul = a * b
    return sum, mul             # 패킹

# 묶어서 
result = sum_and_mul(5,3)
# print(result)
# 언패킹
sum = result[0]
mul = result[1]
print(sum)
print(mul)

# 하나씩 -> 언패킹 사용  (갯수가 안맞으면 오류남)
sum,mul = sum_and_mul(5,3)
print(sum)
print(mul)

print("---------------------")

# 정의
def plus_print(a=0, b=0):
    print(f"{a} + {b} = {a+b}")

# 파라미터를 위치로 매칭
plus_print(3,5)     # a =3, b = 5
plus_print(3)       # a =3, b = 0
plus_print()        # a =0, b = 0

# 파라미터를 이름으로 매칭
# plus_print(,5)      # 오류
plus_print(b=5)         # 앞에는 안쓰고 뒤만 쓰고싶을경우
plus_print(b=5, a=3)

print("---------------------")
"""
sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4,5,6,7)
"""
# 정의  -> 개수를 정의할수 없을때 (몇개올지 모를때 * 사용)
def sum_many (*args):
    #print(type(args))
    sum = 0
    for no in args:
        # sum = sum + no
        sum += no
        #print(no)
    print(sum)
    print("--")


sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4,5,6,7)


print("---------------------")
"""
sum_mul("sum", 1,23,45)
sum_mul("mul", 1,23,45,22,2333)
"""

# 정의  -> 다른 매개변수와 함께 사용할때        * 튜플 리스트로옴 (읽기전용묶음) (갯수가 여러개일때)
def sum_mul(mode, *args):
    # print(mode)
    if mode == "sum":
        #print("sum모드")
        result = 0
        for num in args:
            result += num

    elif mode == "mul":
        result = 1
        for num in args:
            result *= num

    else:
        print("mode를 입력해주세요")

    print("--")
    print(result)           # result가 if 안에 선언됐는데 밖에서도 적용됨

# 사용
sum_mul("sum", 1,23,45)
sum_mul("mul", 1,23,45,22,2333)


print("---------------------")

# 딕션어리 (키-값) 사용한 함수정의
def add_person(hp, **kwargs):
    print(hp)           # 무조건 넣어야함  타입 튜플
    print(kwargs)       # 갯수 상관없는데 키-값으로 넣어줘야함, 순서도 상관없음 타입 딕션어리
    print("--") 

# 사용
add_person("010-1111-1111")
add_person("010-1111-1111", name="정우성")
add_person("010-1111-1111", birth="2000-01-01", name="정우성", company="02-1111-1111")


print("---------------------")
# 두가지 다사용하는 함수정의
def add_person2(*hp, **kwargs):
    print(hp)           # 폰번호 갯수 가변(고정 x)
    print(hp[0])        # 튜플

    print(kwargs)       # 개인정보 종류 갯수 가변
    print(kwargs["name"])   # 딕션어리
    print("---")

# add_person2("010-1111-1111")
# add_person2("010-1111-1111", "010-2222-2222")
add_person2("010-1111-1111", name="정우성")
add_person2("010-1111-1111", age=24, name="정우성")
add_person2("010-1111-1111", age=24, company="(주)우리회사", name="정우성")
# add_person2("010-1111-1111", age=24, company="(주)우리회사", name="정우성", "02-2222-2222")
# 앞에있는건 앞에 몰아줘야함
add_person2("010-1111-1111", "02-2222-2222", age=24, company="(주)우리회사", name="정우성")



