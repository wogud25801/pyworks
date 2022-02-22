# 1~ 100까지의 자연수 중 4의 배수와 개수를 출력하는 프로그램

def get_times(n):
    for i in range(1, 101):
        global count
        if i % 4 == 0:
            count = count + 1
            print(i, end=' ')


count = 0    #배수의 개수
get_times(4)
print("\n배수의 개수 :", count)
