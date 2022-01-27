# 딕셔너리 생성과 사용
# 딕셔너리 자료 구조 - Key와 값의 상으로 이루어짐

person = { } # 빈 딕셔너리

print(person)

# 요소 추가
person['name'] = "오상식"
person['age'] = 26
person['phone'] = "010 - 2483 - 1757"

# 특정 요소 조회
print(person['name'])

# 요소 삭제
del person['phone']

# 요소 수정
person['name'] = "전재홍"

# 전체 요소 조회
for key in person:     
    print(key, ':', person[key])        # 키
   #print(person[key])               # 값
             


print(person)

