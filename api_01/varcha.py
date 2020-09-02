import time
import random

timeDate = time.time()
yearDate = time.strftime("%Y", time.localtime(timeDate))



first_six = ['610524']


# # 输入年份，并判断是否是闰年，并且从1984年开始到现在，输入错误重新输入
# while True:
#         year_int = int(input('请输入年份：'))
#         if year_int < 1984 or year_int > int(yearDate):
#             print('您输入的年份有误，请重新输入')
#         else:
#             break
#
# # 输入月份，2月特殊，输入错误重新输入，如果小于10 返回0x
#
# while True:
#         month_int = int(input('请输入月份：'))
#         if month_int in range(1, 13):
#             break
#         else:
#             print('月份有误，请重新输入！')
#
# # 判断日期，闰年的2月有29天 其他为28天。是否在合理范围内输入错误重新输入，小于10返回0x
#
# while True:
#     day_int = int(input('请输入日期：'))
#     if day_int < 1:
#         print('输入日期有误')
#         continue
#     if month_int == 2:
#         if (year_int % 4 == 0 and year_int % 100 != 0 ) or year_int % 400 == 0:
#             if day_int > 29:
#                 print('您输入%d是闰年，2月只有29天，请重新输入！' % year_int)
#             else:
#                 break
#         else:
#             if day_int > 28:
#                 print('您输入%d不是闰年，2月只有28天，请重新输入！' % year_int)
#             else:
#                 break
#     elif month_int in (4, 6, 9, 11):
#         if day_int > 30:
#             print('输入的日期有误')
#         else:
#             break
#     else:
#         if day_int > 31:
#             print('输入日期有误')
#         else:
#             break



#  第15--17位数字
k = []
for i in range(2):
    j = str(random.randint(0, 9))
    k.append(j)
fale = int(input('请输入性别：1.女  2.男'))
if fale == 2:
    m = str(random.randrange(1, 9, 2))
else:
    m = str(random.randrange(0, 8, 2))
#print(m)

random_str = ("".join(k)+ str(m))
print(random_str)

# TODO 第18位填写







