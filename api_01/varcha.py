import time
import random
import re
# 查看系统时间，身份证不能生成大于当前时间
timeDate = time.time()
yearDate = time.strftime("%Y", time.localtime(timeDate))

# 随机生成身份证前6位

with open('id_card.txt', 'r', encoding='utf-8')as f:
    text = f.read()
    #print(text)

# 处理文本中的数字
text1 = re.findall('\d+', text)
# print(text1)

random_id = text1[random.randint(1, len(text1))]
 # print(random_id)

# 输入年份，并判断是否是闰年，并且从1984年开始到现在，输入错误重新输入
while True:
        year_int = input('请输入年份：')
        if int(year_int) < 1984 or int(year_int) > int(yearDate):
            print('您输入的年份有误，请重新输入')
        else:
            break

# 输入月份，2月特殊，输入错误重新输入，如果小于10 返回0x

while True:
        month_int = int(input('请输入月份：'))
      #  if 0 < int(month_int) < 13:
        if month_int in range(1, 13):
            break
        else:
            print('月份有误，请重新输入！')

# 判断日期，闰年的2月有29天 其他为28天。是否在合理范围内输入错误重新输入，小于10返回0x

while True:
    day_int = input('请输入日期：')
    if int(day_int) < 1:
        print('输入日期有误')
        continue
    if int(month_int) == 2:
        if (int(year_int) % 4 == 0 and int(year_int) % 100 != 0 ) or int(year_int) % 400 == 0:
            if int(day_int) > 29:
                print('您输入%d是闰年，2月只有29天，请重新输入！' % int(year_int))
            else:
                break
        else:
            if int(day_int) > 28:
                print('您输入%d不是闰年，2月只有28天，请重新输入！' % int(year_int))
            else:
                break
    elif int(month_int) in (4, 6, 9, 11):
        if int(day_int) > 30:
            print('输入的日期有误')
        else:
            break
    else:
        if int(day_int) > 31:
            print('输入日期有误')
        else:
            break


def tw(a):
    if a < 10:
        return '0' + str(a)
    else:
        return str(a)
# 出生年月日
y = year_int
m = tw(int(month_int))
d = tw(int(day_int))


birthday = y + m + d


#  第15--17位数字
k = []

for i in range(2):
    j = str(random.randint(0, 9))
    k.append(j)

# 第17位数字 偶数给女性  奇数给男性

fale = input('请输入性别：1.男  2.女')
if int(fale) % 2 == 0:
    m = str(random.randrange(0, 8, 2))
else:
    m = str(random.randrange(1, 9, 2))
#print(m)

random_str = ("".join(k) + str(m))
# print(random_str)

ID_17 = random_id + birthday + random_str

#print(ID_17)
#  第18位填写

# 系数
list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

count = 0
for i in range(17):
    count += int(ID_17[i]) * list[i]

checkNum = count % 11

# 校验码
CheckCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

print(ID_17+CheckCode[checkNum])


# TODO 随机生成10个固定日期的身份证



