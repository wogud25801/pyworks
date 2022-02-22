#몫과 나머지 계산하기
# 변수 입력
bread = 35
people = 4


#계산
몫 = bread // people
나머지 = bread % people

몫2 = int(bread / people)  #int() - 정수로 반환

#출력
print("빵의 개수 :", 몫)
print("빵의 개수 :", 몫2)
print("남은 빵의 개수 :", 나머지)
