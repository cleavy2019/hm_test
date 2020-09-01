import time

timeDate = time.time()
yearDate = time.strftime("%Y", time.localtime(timeDate))

def year():
    while True:
        year_int = int(input('请输入年：'))
        if year_int in range(1980, int(yearDate)+1):
            return year_int
            break
        else:
            print('输入错误，请重新输入')
# 判断月份
def month():
    while True:
        month = int(input('请输入月份：'))
        if month in range(1, 13):
            if month < 10:
                return ('0' + str(month))
            else:
                return month
            break
        else:
            print('您输入错误，请重新输入月份')

# 判断日期
def day():
    while True:
        day_int = int(input('请输入日期：'))
        if day_int in range(1, 32):
            if day_int < 10:
                return ('0' + str(day_int))
            else:
                return day_int
            break
        else:
            print('您输入错误，请重新输入日期')







