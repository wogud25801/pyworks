import re

pattern1 = re.compile("[a-z]+")  #정규 표현식
result = pattern1.match("before") #처음 문자부터 검색
#print(result)
print(result.group())  # group() - 문자열로 반환
print(result.start())  # start() - 첫번 째 인덱스
print(result.span())   # span() - 튜플(시작, 끝 인덱스)

pattern2 = re.compile("[0-9]+\s[a-z]+")
result2 = pattern2.match("2022 python")
#print(result2)
print(result2.group())
print(result2.end)