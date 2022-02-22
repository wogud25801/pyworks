# 재귀함수 - 자기 자신을 호출하는 함수
# 반복되므로 종료 조건이 필요

def sos(i):
    print("Help Me!!")
    if i == 1:    #종료 조건(마지막 횟수)
        return ""
    else:
        return sos(i - 1)
sos(5)
