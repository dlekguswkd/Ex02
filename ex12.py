# 프로그램 예외처리

num = int(input("숫자를 입력하세요\n"))
# try catch 에러메세지 
try:                                # 실행문
    result = 100/num
    print(result)
except ZeroDivisionError as e:      # 예외 처리문
    print(e)
finally:                            # 예외 발생 여부와 상관없이 무조건 실행되는 문장 (생략가능)
    print("공통영역")                # 예외 처리문에 없는 오류가 나도 여기는 실행된다
    
print("프로그램 정상종료")



