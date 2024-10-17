# 집합(set) 셋

# 셋 {} 중복이 있으면 안된다 순서가 없다 -> 방번호의 개념 없음 (시퀀스(순서) 자료형이 아님) 
# set도 수정이 안됨
# {}에 키:값이 있으면 딕션어리, 값만 있으면 셋

print("=== set 셋 ====================")

no_list = {1,2,3}
print(no_list, type(no_list))

print(len(no_list))       # 갯수

print( 2 in no_list)              # a에 2가 있냐
print( 2 not in no_list)          # a에 2가 없냐
# print(a[2])               오류 여기는 방번호의 개념이 없음


print("=== set 메소드 ====================")
no_list.add(100)            # 추가 (한개)
print(no_list)              # 순서 의미없음

no_list.add(3)              # 추가 이미 있는거 넣기
print(no_list)              # 이미 있는 값은 추가되지 않는다


no_list.discard(100)        # 삭제      -> 없는값이면 지우지않고 그냥 넘어감
print(no_list)              # 값 100 이 삭제됨

#no_list.remove(100)        # 삭제      -> 없는값이면 에러뜸
print(no_list)              # 값 100 이 삭제됨


no_list.update({888, 999})      # 추가  (여러개)
print(no_list)                  

no_list.clear()                 # 다지우기
print(no_list)                  


print("=== set 집합개념 ====================")
s1 = {1, 2 , 3, 4, 5, 6, 7, 10}
s2 = {10, 20, 30}

print(type(s1), type(s2))

# 두가지 똑같음
s3 = s1.union(s2)       # 합집합
print(s3)               # 중복되는건 한번만 나옴
s3 = s1 | s2            # 합집합  또는
print(s3)


# 두가지 똑같음
s4 = s1.intersection(s2)    # 교집합
s4 = s1 & s2                # 그리고
print(s4)


# 두가지 똑같음
s5 = s1.difference(s2)      #차집합 s1-s2
s5 = s1-s2
print(s5)

s6 = s2.difference(s1)      #차집합 s2-s1
s6 = s2-s1
print(s6)



