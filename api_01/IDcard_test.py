import time
import random

    # 身份证前6位
for_six = ['610524']
    # 出生年月

    # print(yearDate)
def birthday_year():
    timeDate = time.time()
    yearDate = time.strftime("%Y", time.localtime(timeDate))
    yearNum = random.randint(1980, int(yearDate))
    return str(yearNum)
def birthday_month():
    monthNum = random.randint(1, 12)
    if monthNum < 10:
        return ('0'+ str(monthNum))
    else:
        return (str(monthNum))
def brithday_day():
    year = birthday_year()
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        dayNum = random.randint(1, 31)
        if dayNum < 10:
            return ('0'+ str(dayNum))
        else:
            return (str(dayNum))


birthday = birthday_year()+birthday_month()+brithday_day()
print(birthday)


    # 身份证后三位

    # 最后一位校验码





