# 입력받아 파일에 쓰기
# 추가 모드 - 'a'
with open('./output/input.txt', 'a') as f:
    text = input("저장할 내용을 입력하세요 : ")
    f.write(text)
    f.write('\n')
