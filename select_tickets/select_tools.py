

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

tickets = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,
           11,	12,	13,	14,	15,	16,	17,	18,	19,	20,
           21,	22,	23,	24,	25,	26,	27,	28,	29,	30,
           31,	32,	33,	34,	35,	36,	37,	38,	39,	40,
           41,	42,	43,	44,	45,	46,	47,	48,	49,	50,
           51,	52,	53,	54,	55,	56,	57,	58,	59,	60,
           61,	62,	63,	64,	65,	66,	67,	68,	69,	70,
           71,	72,	73,	74,	75,	76,	77,	78,	79,	80,
           81,	82,	83,	84,	85,	86,	87,	88,	89,	90,
           91,	92,	93,	94,	95,	96,	97,	98,	99,	100]
# 显示电影票
# 如果座位被占用，用**代替，其他正常输出
# 查看座位的时候不显示已经被占用的座位号

def show_tickets():
    print('荧幕'.center(45))
    print('')
    for i in range(len(tickets)):
        if (i + 1) % 10 == 0:
            print(tickets[i], end="\n")
        else:
            print(tickets[i], end="\t")

# 选择电影票
def select_tickes(ticket_no):

        if int(ticket_no) in range(1, 101) and tickets[int(ticket_no) - 1] != '**':  # tickets[int(ticket_no) - 1] 票号是1，角标是0
            print('您选择的座位号是【%s】' % ticket_no)
            tickets[int(ticket_no)-1] = '**'

        else:
            print('您选择的座位号有误，请重新选择！')
            return False
# 退票
def checkout_tickets(out_ticket):

        if int(out_ticket) in range(1, 101) and tickets[int(out_ticket) - 1] == "**":
            print(('您申请的退票号是：%s') % out_ticket)
            print('申请退票成功')
            tickets[int(out_ticket) - 1] = out_ticket    # 将out_ticket 重新赋值给tickets[int(out_ticket) - 1]

        else:
            print('您申请的退票号不存在，请重新输入！')
            return False





