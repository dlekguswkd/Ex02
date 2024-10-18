# 모듈 불러다 쓰기

import mymath       # 파일명  불러오면 거기에 있는것도 실행됨
# import mymath as mm       이런식으로 할수있음 대신 밑에 이름들도 mm으로 (이름이 길때 유용)

# __name__  mymath 이라고 찍음

print("--main--")

print(mymath.plus(10,10))       # 더하기
print(mymath.minus(10,10))      # 빼기
print(mymath.div(10,10))        # 나누기
print(mymath.multi(10,10))      # 곱하기
print(mymath.area_circle(10))   # 원의 넓이