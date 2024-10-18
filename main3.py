# 모듈 불러다 쓰기

from mymath import plus, minus as m        # 파일명  불러오면 거기에 있는것도 실행됨 -> 특정 이름만


print("--main--")                       # 대신 모듈이름. 을 제외해야함  안불러온건 사용불가

print(plus(10,10))       # 더하기
print(m(10,10))      # 빼기
# print(mymath.div(10,10))        # 나누기          불러오지 않아서 사용불가
# print(mymath.multi(10,10))      # 곱하기
# print(mymath.area_circle(10))   # 원의 넓이