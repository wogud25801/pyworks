# 튜플의 생성 및 사용

# 튜플의 생성
t1 = (1, )                  # 1개만 저장할 때 콤머( , )를 뒤에 붙임
t2 = (2, 3, 4)
t3 = t1 + t2

# 출력
print(t1)
print(t2)
print(t3)

# 인덱싱과 슬라이싱
print(t3[0])
print(t3[:2])
print(t3[2:])

# 요소 수정 - 불가
#t3[1] = 5

# 요소 삭제 - 불가
#del t3[2]

