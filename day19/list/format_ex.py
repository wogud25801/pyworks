#문자열 출력함수 - format()
print("I eat {} apples".format(3))

n = 5
print("I eat {} apples".format(n))

day = 2
print("I ate {0} apples. so I was sick for {1} days".format(n, day))

#'+' 연산자로 출력
sentence = "I ate " + str(n) + " apples. so I was sick for " + str(day) + " days"
print(sentence)
print('='*40)

#회원 정보 출력하기
name = input("이름 : ")
user_id = input("아이디 : ")
user_pw = input("비밀번호 : ")
user_pw = '*' * len(user_pw) #'*'로 문자열 감추기

print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
print("비밀번호 : {}".format(user_pw))
