import re
# 이름과 전화번호를 분리
# ()는 그룹으로 분리
str01 = "jang 010-2483-1757"
pat = re.compile("(\w+)\s+(\d{3}[-]\d{4}[-]\d{4})")
m = pat.match(str01)
print(m.group())
print(m.group(1))  #group(인덱스번호)
print(m.group(2))

# group(그룹이름)
pat2 = re.compile("(?P<name>\w+)\s(?P<phone>\d{3}[-]\d{4}[-]\d{4})")
m2 = pat2.match(str01)
print(m2.group("name"))
print(m2.group("phone"))