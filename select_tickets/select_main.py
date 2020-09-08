from select_tickets import select_tools

while True:

    # 展示电影院的所有座位
    select_tools.show_mune()

    action = input('请选择您的操作：')
    if action.isdigit():
        # 查看座位号 1
        if action == 1:
            while True:
                ticket_no = input('请选择您的座位号(1-100)：')
                if ticket_no.isdigit():
                    if select_tools.select_tickes(ticket_no) is not False:
                        break
                else:
                    print('请按说明操作1')
    # 选择座位号 2
        elif action == 2:
            select_tools.show_tickets()
    # 退票 3
        elif action == 3:
            while True:
                out_ticket = input('请输入您要申请的退票号：')
                if out_ticket.isdigit():
                    if select_tools.checkout_tickets(out_ticket) is not False:
                        break
                else:
                    print('请按说明操作2')
        # 返回主页面 0
        elif action == 0:
            print('欢迎您再次使用影院订票系统，祝您观影愉快！！！')
            break
        else:
            print('您输入有误，请重新输入')
    else:
        print('请按说明操作！')