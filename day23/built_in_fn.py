# 내장 함수
# all() - 요소중 0이 없으면 모두 참이다.
print(all([1, 5, 3]))
print(all([1, 0, 3]))

#any() - 모두 0일때만 False임,
print(any([1, 2, 0]))

# round(n, digit) - digit를 생략하면 정수로 반올림
# 소수 자리수를 표시할때 digit 값 설정
print(round(4.6))
print(round(4.67, 1))

# eval(표현식) - 문자열을 숫자로 변환
x = 1
print(eval("x + 1"))

# list(str) - 문자열을 리스트로 변환
print(list("python"))

# sum(iterable) - 반복가능한 자료 더하기
print(sum([70, 80, 90]))

# min(iterable) - 최소값
print(min([70, 80, 90]))

# 거듭 제곱
print(pow(2, 4))