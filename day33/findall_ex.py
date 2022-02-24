import re

str = "123?45yy7890 Hello"

m1 = re.findall("\d{1,3}", str)  # 각각 1, 2, 3개인것 일치, {}안 띄어쓰면 못찾음
print(m1)

m2 = re.findall("[A-Za-z]+", str)  # +는 반복의 개념
print(m2)

m3 = re.finditer("[A-Za-z]+", str) # finditer()는 객체로 반환
print(m3)
for i in m3:
    print(i)