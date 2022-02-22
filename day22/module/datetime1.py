import datetime
import calendar as cal

# 오늘 날짜와 현재 시간
now = datetime.datetime.today()
print(now)

# 날짜
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))

# 시간
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

# 오늘 날짜
today = datetime.date.today()
print(today)

# 특정한 날짜
the_day = datetime.date(2022, 1, 1)
print(the_day)

# 달력
cal.prcal(2021)      # 전체 출력
cal.prmonth(2022, 2) # 특정 달 출력