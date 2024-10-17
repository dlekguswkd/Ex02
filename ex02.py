print("=== 튜플(tuple) 기본 ====================")

# a = [1,2,3,4]   -> 리스트

# 튜플  -> 수정불가
t = (1, 2, 3, 4)
print(type(t))          # <class 'tuple'>

# 수정불가, 읽기는 가능
print(t[0], t[1], t[2])             # + index
print(t[-1], t[-2])                 # - index

print(t[1:3])                       # (2, 3)    -> 튜플
print(t[:])                         # 튜플 처음부터 끝까지

print(t*2)                          # 원본이 바뀌는거 아님 한번 더 추가됨
print(t)                            # 원본 바뀌지않음 (수정의 개념이 아님)

print(t + (100, 200, 300))          # 원본이 바뀌는거 아님 뒤에 추가됨
print(t)                            # 원본 바뀌지않음 (수정의 개념이 아님)

print(len(t))                       # 갯수 알아내기
print(5 in t)                       # t에 5가 있냐?  False True 로 리턴



print("=== 튜플 생성 ====================")
t = (1, 2, 3, 4)                # a = [1,2,3,4]   -> 리스트


tt = 100, 200, 300              # 이렇게 하면 튜플로 됨 (리스트 x)
print(tt)

t = (99)            # -> t = 99 랑 똑같아짐  튜플인지 모름 숫자가 하나일때 생기는 일
print(t)            # 값이 하나만 있을때는 숫자다
t = (99,)           # 튜플하고싶은데 하나일땐 뒤에 , 넣어주기
print(t)            # 값이 한개일때 튜플 생성방법


print("=== 튜플 값 변경 (x) ====================")
t = ("apple", "banana", 10, 20)

# t[0] = "mango"        # 튜플은 수정이 불가해서 에러뜸
# t[2] = 100
print(t[2]+10)          # 원본의 값이 바뀌는게 아니라 가능

# t[1:2] = (1000, 2000)     # 원본이 변하는건 다 불가

a_list = list(t)            # 튜플을 리스트로 바꾸기
print(type(t))
print(type(a_list))


t = ("apple", "banana", 10, 20)
for item in t:
    print(item)

for index, item in enumerate(t):
    print(index, item)