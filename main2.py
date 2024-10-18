# 모듈 불러다 쓰기

import mymath as mm       # 파일명  불러오면 거기에 있는것도 실행됨 -> 별명으로 

print("--main--")

print(mm.plus(10,10))       # 더하기
print(mm.minus(10,10))      # 빼기
print(mm.div(10,10))        # 나누기
print(mm.multi(10,10))      # 곱하기
print(mm.area_circle(10))   # 원의 넓이