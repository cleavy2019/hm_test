
# 展示主系统
def show_mune():
    print('*' * 50)
    print('欢迎进入电影院订票系统'.center(40))
    print('1. 选择座位号')
    print('2. 查看剩余座位号')
    print('3. 退票')
    print('')
    print('0 是退出系统')
    print('*' * 50)


# 显示电影票
def show_tickets():
    print('荧幕'.center(45))
    print('')
    results = range(1, 101)
    for i in range(len(results)):
        print(str(results[i]).rjust(2, '0').center(4), end=',')
        if results[i] % 10 == 0:
            print('\n')

# 如果座位被占用，用**代替，其他正常输出


# 查看座位的时候不显示已经被占用的座位号


# 选择电影票
def select_tickes():
    while True:
        ticket_no = input('请选择您的座位号(1-100)：')
        if int(ticket_no) in range(1, 101):
            if int(ticket_no) < 10:
                print('您选择的作为号是【%s】' % ('0'+ticket_no))
            else:
                print('您选择的作为号是【%s】' % ticket_no)
            return ticket_no
        else:
            print('您选择的座位号有误，请重新选择！')


# 退票

def checkout_tickets(x):
    while True:
        t = input('请输入您要申请的退票号：')
        if int(t) in range(1, 101) and t == x :
            print(('您申请的退票号是：%s') % t)
            print('申请退票成功')
            break
        else:
            print('您申请的退票号不存在，请重新输入！')






