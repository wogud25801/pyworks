#놀이공원 입장료 계산
print("♣ 놀이 공원 입장료 계산 ♣")

#입력
age = int(input("나이를 입력해 주세요 : "))
charge = 0

#if ~ elif ~ else 구문
if age < 8:
    print("미취학 아동입니다.")
    charge = 1000
elif age >= 8 and age < 14:
    print("초등학생 입니다.")
    charge = 2000
elif age >= 14 and age < 20:
    print("중,고등학생 입니다.")
    charge = 2500
else:
    print("일반인 입니다.")
    charge = 3000

print("입장료는 " + str(charge) + "원입니다.")


