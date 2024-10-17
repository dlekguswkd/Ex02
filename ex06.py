# 형변환

t = (1,2,3)     # 읽기전용 튜플 ()
print(t)
print(type(t))
# t[1] = 100      # 오류뜸  수정안됨

# tuple --> list
a_list = list(t)        # 리스트로 담기 []
print(a_list)
print(type(a_list))
a_list[1] = 100
print(a_list)           # 수정됨
print(t)                # t는 튜플로 원본 변경되지않음


# list --> tuple
a = [1,2,3,1]
print(type(a))
print(a)            # []

t_tuple = tuple(a)
print(t_tuple)          # ()

# t_tuple[1] = 999          오류뜸 튜플이라서 수정불가


# tuple --> set  읽기전용 -> 중복안되는걸로
t = (1,2,3,1)         # ()
print(t)

s_set = set(t)
print(s_set)        # {}        중복되는건 하나만 표현됨

