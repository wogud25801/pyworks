# 문자열 출력함수 - format()
print("I eat {} apples".format(3))

n = 5
print("I eat {} apples".format(n))

day = 2
print("I eat {} apples. so i was sick for {} days".format(n, day))

# '+' 연산자로 출력
sentence ="I eat " + str(n) + " apples. so i was sick for " + str(day) + " days "
print(sentence)
print('=' * 40)

# 회원 정보 출력하기
name = input("이름 : ")
user_id = input("아이디 : ")
user_pw = input("비밀번호 : ")
user_pw = '*' * len(user_pw) # '*'로 문자열 감추기

name = input("이름 :{}". format(name))
name = input("아이디 :{}". format(user_id))
name = input("비밀 번호:{}". format(user_pw))
