# f.close()를 사용하지 않는 구분
# with open(파일 경로) as 파일 객체
with open('./output/text.txt', 'w') as f:
    f.write("안녕하세요\n")
    f.write("Have a nice day!!")

with open('./output/text.txt', 'r') as f:
    text = f.read()
    print(text)