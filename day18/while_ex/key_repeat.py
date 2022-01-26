#키 반복 동작
while True:
    key = input("반복을 계속 할까요?(y/n)")
    if key == 'y' or key == 'Y':
        print("반복을 계속 합니다.")
    elif key == 'n' or key == 'N':  print("i=", i, ", sum_v =", sum_v)

        print("반복을 중단합니다.")
        break
    else:
        print("키를 잘못 눌렀습니다.")
