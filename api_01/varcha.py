import random
import re
import time
# 查看系统时间，身份证不能生成大于当前时间
timeDate = time.time()
yearDate = time.strftime("%Y", time.localtime(timeDate))


# 输入年份，并判断是否是闰年，并且从1984年开始到现在，输入错误重新输入
while True:
    y = input('请输入年份(1984-现在）：')
    if int(y) < 1984 or int(y) > int(yearDate):
        print('您输入的年份有误，请重新输入')
    else:
        break

# 输入月份，2月特殊，输入错误重新输入，如果小于10 返回0x

while True:
    m = input('请输入月份：')
    if int(m) in range(1, 13):
        break
    else:
        print('月份有误，请重新输入！')

# 判断日期，闰年的2月有29天 其他为28天。是否在合理范围内输入错误重新输入，小于10返回0x

while True:
    d = input('请输入日期：')
    if int(d) < 1:
        print('输入日期有误')
        continue
    if int(m) == 2:
        if (int(y) % 4 == 0 and int(y) % 100 != 0 ) or int(y) % 400 == 0:
            if int(d) > 29:
                print('您输入%d是闰年，2月只有29天，请重新输入！' % int(y))
            else:
                break
        else:
            if int(d) > 28:
                print('您输入%d不是闰年，2月只有28天，请重新输入！' % int(y))
            else:
                break
    elif int(m) in (4, 6, 9, 11):
        if int(d) > 30:
            print('输入的日期有误')
        else:
            break
    else:
        if int(d) > 31:
            print('输入日期有误')
        else:
            break
fale = input('请输入性别：1.男  2.女')
num = int(input('您希望获得多少身份证号：'))


def qian_six():
# 随机生成身份证前6位

    with open('id_card.txt', 'r', encoding='utf-8')as f:
        text = f.read()
    
    # 处理文本中的数字
    text1 = re.findall('\d+', text)
    
    random_id = text1[random.randint(1, len(text1))]
    return random_id

# 如果 月 和日 小于10 返回 0X 。
def tw(a):
    if int(a) < 10:
        return '0' + str(a)
    else:
        return str(a)

#  第15--17位数字

def hou_san(a):
    k = []
    for i in range(2):
        j = str(random.randint(0, 9))
        k.append(j)

    # 第17位数字 偶数给女性  奇数给男性

    if int(a) % 2 == 0:
        m = str(random.randrange(0, 8, 2))
    else:
        m = str(random.randrange(1, 9, 2))

    random_str = ("".join(k) + str(m))

    return random_str

# 前17位数字
def fifth_seven(a,b,c):
    return (qian_six()+ tw(a) + tw(b) + tw(c) + hou_san(fale))
#  第18位填写


def hou_one():
# 系数

    xishu = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    str = fifth_seven(y, m, d)
    list1 = list(str)
    numbers = list(map(int, list1))
    print(numbers)
    func = lambda x, y: x*y
    result = map(func, xishu, numbers)
    list_result = list(result)
    print(sum(list_result))


    checkNum = sum(list_result) % 11
    print(checkNum)

    # TODO 校验码重新计算
    CheckCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

    return CheckCode[checkNum]



six = qian_six()
birthday = y + tw(m) + tw(d)
fifth = hou_san(int(fale))
last = hou_one()

print(six + birthday + fifth + last)




