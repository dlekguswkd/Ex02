# 패킹과 언패킹

print("=== 패킹과 언패킹 ====================")

'''
z01 = 10
z02 = 20
z03 = "python"

t = [z01, z02, z03]
print(t)
'''

# 패킹
t = 10, 20, "python"        # 튜플로 묶어서 변수에 할당  * 읽기전용 리스트
print(t, type(t))

# t[2] = "java"           # 오류남 튜플은 수정이 안되기때문 튜플이라서 값을 바꿀수 없다

# l = list(t)             # 원본은 안바뀌고 리스트로 바꿔주는거임
# print(type(l))

print(t[0], t[1], t[2])     

'''
item01 = t[0]
item02 = t[1]
item03 = t[2]
print(item01)
print(item02)
print(item03)
'''
# 언패킹
item01, item02, item03 = t
print(item01)
print(item02)
print(item03)

