# 파일 쓰기 - 파일 생성

# 파일 열기 - open(경로, 추가모드)
f = open("c:/pyfile/test.txt", 'a')

# 파일 쓰기
f.write("안녕하세요\n")

# 파일 닫기
f.close()