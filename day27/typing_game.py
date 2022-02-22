# 영어 타자 게임
import random
import time
# 외부의 word.txt 읽기

try:
    f = open("./output/word.txt", 'r')
    word = f.read().split()  # 단어를 리스트로 저장함

    n = 1  #문제 번호

    print('[타자 게임] 준비되면 엔터')
    input()
    start = time.time()  #시작 시간
    while n < 11:
        print("문제", n)
        question = random.choice(word)  # 문제
        print(question)
        answer = input()   #사용자가 입력
        # if문 처리
        if question == answer:
            print("통과!")
            n += 1  # 다음 문제
        else:
            print("오타! 다시 도전!")
    end = time.time()  #끝난 시간
    print("타자 시간 : %.2f초"  % (end - start))
except:
    print("파일을 열 수 없습니다.")