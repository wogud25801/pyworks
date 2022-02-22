import sys

args = sys.argv[1:]

total = 0
for i in args:
    total += int(i)  # 입력받은 문자를 숫자로 변환

print(total)
