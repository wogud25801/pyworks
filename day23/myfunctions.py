# 함수 만들기
# 절대값 함수
def myabs(x):
    if x < 0:
        return -x
    else:
        return x

# 거듭제곱 함수
def mypow(x, y):
    num = 1
    for i in range(0, y):
        num *= x
        print("i =", i, ", num =", num)
    return num

if __name__=="__main__":
    # 절대값 호출
    print(myabs(-10))

    # 거듭제곱 호출
    print(mypow(2, 4))  #2x2x2x2
    print(mypow(5, 3))  #5x5x5