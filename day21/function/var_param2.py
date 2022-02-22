# 가변 매개변수
"""
매개변수의 입력값이 정해지지 않고 변경해야 할때 사용하는 변수
변수이름 앞에 '*'를 붙임
"""
def merge_text(*text):
    result = ""    #문자 초기화
    for txt in text:
        result += txt

    return result
        
str1 = merge_text("모자", "장갑")
str2 = merge_text("모자", "장갑", "목도리")

print(str1)
print(str2)

