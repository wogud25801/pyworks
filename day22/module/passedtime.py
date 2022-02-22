import datetime

print(" ♠ 지금까지 몇 일? ♠")
day1 = datetime.date(2021, 12, 26)
print(day1)

today = datetime.date.today()

# 지나온 날
passedtime = today - day1
print(passedtime)
print("개강 이후 {}일이 지났습니다.".format(passedtime.days))