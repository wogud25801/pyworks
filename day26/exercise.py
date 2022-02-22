# Q1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(10))  #False
print(is_odd(11))  #True

# Q2 - 가변 매개 변수
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args) #평균 = 합계 / 개수

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# Q3
"""
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)
"""

# 04
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")

# join - 리스트를 문자열로 변환하는 함수
print("".join(["you", "need", "python"]))