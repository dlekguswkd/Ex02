# 자료구조  리스트
# 리스트 [] 순서가 있다  index  슬라이싱
print("=== 리스트 기본 ========================")

test_List = [1, 12, 123, 1234]

print(type(test_List))      # type  --> <class 'list'>

print(test_List[0], test_List[3])
print(test_List[-1])        # -인덱스

print(test_List[1:3])       # 1번방부터 (3-1)번방까지 슬라이싱 문법 가능

print(len(test_List))       # len() 메소드로 갯수 알아내기  

print(test_List*2)          # 한번더 담김 있는게 더 담김 
print((test_List*2)[5])          # 한번더 담긴거에 5번째방
print(test_List)            # 원본이 바뀌진않음

print(test_List + [100, 200, 300])          # 리스트에 추가됨
print(test_List)            # 원본이 바뀌진않음

print(2 in test_List)       # 배열에 있냐? 
result = 12 in test_List    # 배열에 12가 있으면 true
print(result)

print("=== 리스트 삭제 ====================")
# del(test_List[2])
# del test_List[2]  같은 표현
print(test_List)        # 원본이 바뀜


print("=== 리스트 수정 ====================")
test_List[0] = "apple"      # 자료형이 다른것도 들어감
print(test_List)

b_list = ["apple", "banna", 10, 20]
b_list[2] = b_list[2] + 90      
print(b_list)


print("=== 리스트 수정 ====================")
test_List = [1, 12, 123, 1234]
print(test_List[0:2])       # [1, 12]
test_List[0:2] = [888, 999]
print(test_List)            # 원본이 바뀜

print(test_List[0:2])       # [888, 999]
test_List[0:2] = [777]
print(test_List)            # 자리수가 안맞아도 두개짜리를 하나로 바꿔버림
print(test_List[0:2])       # [777, 123]

test_List[2:3] = [111]
print(test_List)

# 추가
test_List[2:3] = ["aaa", "bbb", "ccc"]      # 갯수가 안맞아도 (모자라도) 그냥 늘어남
print(test_List)            # [777, 123, 'aaa', 'bbb', 'ccc']



print("=== 슬라이스를 통한 삭제 ====================")
a = [1, 12, 123, 1234]
a[1:2] = []     # 1번째 방 삭제
print(a)

# 처음부터 끝까지
a[0:] = []
print(a)


print("=== 슬라이스를 통한 삽입 ====================")
a = [1, 12, 123, 1234]
#  [1, "a", 12, 123, 1234] 이렇게 하고싶음
# a[1:2] = "a"      # 이건 수정개념 12가 a 로 바뀜  a[1:2] -> a[1:1] -> a[1]
print(a)

a[1:1] = 'a'        # 이건 추가개념 a[1:1] -> a[1:0]
print(a)

a[5:] = [12345]     # 5번쨰방이 없는데도 추가됨
print(a)

a[:0] = [-12, -1, 0]    # 맨앞에 추가  [:] 앞뒤 번호가 같으면 추가의 개념
print(a)

# 슬라이싱 문법 방번호가 같으면 추가 ex) [3:3]


print("=== 리스트의 메소드 사용 ====================")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a) 

# 추가
a.append("정우성")      # 맨끝에 추가됨  -> append는 하나만 추가 가능
print(a)

a.insert(2, "박명수")       # 2번째 방에 추가해줘 나머지는 하나씩 밀림
print(a)

a.extend([6,7,8])       # 맨끝에 추가됨  -> 여러개 추가하고싶을땐 extend 사용해야함
print(a)


# 삭제
a.remove(1000)          # 값으로 찾아서 삭제 내가딱 지정해주는게 사라짐
print(a)

a.pop(6)                # 방번호를 찾아서 삭제 여기에서 6은 6번째방을 의미      del(a[6])
print(a)

a.pop()                # 방번호(X)로 지우기  -> 방번호를 안적으면 마지막꺼가 사라짐
print(a)


print("=== 리스트의 메소드 사용 ====================")
b = [1, 123, 1000, 12, 1000]
print(b)

# 카운트
print(b.count(1000))        # 리스트에 1000 이 몇개있는지

# 뒤집기
b.reverse()                 # 원본 리스트의 순서가 뒤집힌다
print(b)                    # 순서가 반대가됨 -> 원본이 바뀜

# 정렬
b.sort()                    # 오름차순으로 정렬된다
print(b)                    # 원본 리스트가 오름차순으로 바뀜

b.sort(reverse=True)        # 원본 리스트가 내림차순으로 정렬된다
print(b)

# 값으로 index 번호 찾기
print(b.index(1000))        # 처음 검색되는 방번호 리턴


b = [1, 123, 1000, 12, 1000]
for no in b:
    print(no)


for index,no in enumerate(b):
    print(index, no)
