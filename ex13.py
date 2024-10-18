# 파일 읽기

# 이효리   010-2222-3333    031-2323-4441
# 정우성   010-2323-2323    02-5555-5555


print("--파일 한번에 읽기-----")
# 파일 열기 file = open(파일경로, 모드, encoding='utf-8')
file_path = "C:\\javaStudy\\workspace-python\\Ex02\\PhoneDB.txt"
            # \\ 이건 두개씩해야 \ 이거라고 생각함
# 내가정한이름 =        읽기모드    
file = open(file_path, "r", encoding="utf-8")

# 파일 한번에 읽기
# 내가정한이름 = 
data = file.read()
print(data)

file.close()        # 닫아줘야 좋은 코드


# 파일 한번에 읽기2     (with 문 사용) -> close생략이 가능해짐  (간결해짐)
print("--파일 한번에 읽기2-----")
with open(file_path, "r", encoding='utf-8') as file:
    data = file.read()
    print(data)



# 파일 한줄씩 읽기
print("--파일 한줄씩 읽기-----")
file = open(file_path, "r", encoding="utf-8")
#   내가정한이름 line
for line in file:
    print(line.strip())         # strip()  줄바꿈,공백,탭 삭제
file.close()



# 파일 한줄씩 읽기2
print("--파일 한줄씩 읽기2-----")
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
