# 행렬에서 숫자 증가
row = 5
col = 5
for i in range(0, row):
    for j in range(1, col+1):
        num = i * col + j
        print("좌석" + str(num), end=' ')
    print()
