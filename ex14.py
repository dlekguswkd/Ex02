# 파일 쓰기

file_path = "C:\\javaStudy\\workspace-python\\Ex02\\song.txt"

#                      쓰기모드 (백지화됨)      -> 실행될때마다 백지됐다가 다시쓰는거임(추가가안됨)
with open(file_path, "w", encoding="utf-8") as file:
    file.write("학교종이 땡땡땡\n")
    file.write("어서모이자\n")
    file.write("선생님이 우리를\n")
    file.write("기다리신다\n")


