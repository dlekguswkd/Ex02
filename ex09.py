# while 문

# 반복의 횟수를 알 수 없을때 while 반복문
# 반복의 횟수를 알 수 있을때 for 반복문

# 6의 배수이자 14의 배수인 가장 적은 정수 찾기

i = 1
while True :

    if i%6 == 0 and i%14 ==0:       # 6의배수이면서 14의 배수
        print(i)
        break   # 나가기 (멈추기)
    i += 1      # i = i + 1



