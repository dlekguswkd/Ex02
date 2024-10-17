# 딕션어리  키-값
# 딕션어리 {} 키-값 순서가 없다  키중요 (키-리스트 있어야 전체출력가능)


print("=== 사전(dict) :딕션어리 ====================")

a = {}          # 딕션어리 생성방법

# 추가
# "r38" "빅데이터반"
#  키       값
a["r38"] = "빅데이터반"
a["r32"] = "플스택반"
a["r30"] = "진소영"

print(a) 
print(type(a))              # <class 'dict'>

# 생성방법
d = {"basketball": 5, "soccer": 11, "baseball": 9}      # 처음부터 넣고 생성
d["volleyball"] = 6                                     # 추가
print(d)

print("=== 딕션어리 값 출력 ====================")
print(a["r30"])         # 키로 값찾기
print(d["soccer"])
# print(d.get("soccer"))      # 위에꺼랑 같은표현 


print("=== 딕션어리 값 삭제 -> 키 ====================")
print(d)
# del(d["soccer"])      두가지 다 가능
# d.pop("soccer")
print(d)

print("=== 딕션어리 값 삭제 -> 전체 ====================")
d = {"basketball": 5, "soccer": 11, "baseball": 9}   
print(d)

# 다 지우는법 두가지 다 가능
# d ={}
d.clear()
print(d)


print("=== 딕션어리 찾기(검색) ====================")
d = {"basketball": 5, "soccer": 11, "baseball": 9}   
print(d)
print(len(d))           # 갯수
print("soccer" in d)        # 키 값중에 d에 soccer  라는아이가 있니?
print("soccer" not in d)     # 키 값중에 d에 soccer  라는아이가 없니?


print("=== 딕션어리의 키들을 리스트로 반환 ====================") # 키들의 이름을 모를때
d = {"basketball": 5, "soccer": 11, "baseball": 9}   
print(d)

# 내가정한이름 = 메소드에 있는 이름keys
keys = d.keys()
print(keys, type(keys))


# 키를 리스트로 갖고있어야함
#   하나담을 내가정한이름  in 전체이름
for key in keys:
    print(key)              # 키뿌리기
    print(d[key])           # 값뿌리기
    #print(f"{key} ->  {d[key]}")        # 키와, 값 뿌리기


print("=== 딕션어리의 값들을 리스트로 반환 ====================")

# 내가정한이름  = 메소드에 있는 값 values
values = d.values()         # 값들만 뽑기
print(values)       # 순서는 마음대로 나옴
print(type(values))

for value in values:
    print(value)



# 딕션어리는 방번호의 개념이 없음 -> 이걸로 리스트처럼 
play_list = d.items()
print(play_list, type(play_list))

