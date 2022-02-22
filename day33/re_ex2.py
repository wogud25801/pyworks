import re

str1 = "Two is too"

m1 = re.findall("T[wo]o", str1) #리스트로 반환
print(m1)

m2 = re.findall("T[wo]o", str1, re.IGNORECASE) #IGNORECASE- 대소문자 허용
print(m2)