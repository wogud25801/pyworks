# 파일 읽기 - 읽기 모드 : r

try:
    f = open("c:/pyfile/test.txt", 'r')
    text = f.read()
    print(text)
    f.close()

    f = open("c:/pyfile/number.txt", 'r')
    data = f.read()
    print(data)
    f.close()
except FileExistsError:
    print("파일을 열 수 없습니다.")


