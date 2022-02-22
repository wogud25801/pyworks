# 구구단 출력
#print("단 입력 : ")
dan = int(input("단 입력 : "))
for i in range(1, 10):
    #print(dan, 'x', i, '=', (dan * i))
    print("{} x {} = {}".format(dan, i, dan * i))
