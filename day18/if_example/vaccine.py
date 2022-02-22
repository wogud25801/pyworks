#백신 접종자 분류
#나이가 20~65세는 '접종대상자', 아니면 '하반기 일정 확인'
#접종 대상자인 경우 출생년도 끝자리로 분류

#출생 년도 입력
birth_year = input("출생년도 입력 : ")
#print(birth_year[3])

#나이 계산
age = 2022 - int(birth_year) + 1

#if 처리 및 출력
if age >= 20 and age <= 65:
    print("접종 대상자임")
    if birth_year[3] == "1" or birth_year[3] == "6":
        print("월요일 접종")
    elif birth_year[3] == "2" or birth_year[3] == "7":
        print("화요일 접종")
    elif birth_year[3] == "3" or birth_year[3] == "8":
        print("수요일 접종")
    elif birth_year[3] == "4" or birth_year[3] == "9":
        print("목요일 접종")
    elif birth_year[3] == "5" or birth_year[3] == "0":
        print("금요일 접종")
    
else:
    print("하반기 일정 확인")


