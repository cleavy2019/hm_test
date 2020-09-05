from select_tickets import select_tools

print('荧幕'.center(45))
print('')
print('')
results = range(1, 101)
for i in range(len(results)):
    print(str(results[i]).rjust(2, '0').center(4), end=',')
    if results[i] % 10 == 0:
        print('\n')

while True:

    # 展示电影院的所有座位
    select_tools.show_mune()

    action = int(input('请选择您的操作：'))

    # 查看座位号 1
    if action in range(4):
        if action == 1:
            select_tools.select_tickes()
    # 选择座位号 2
        elif action == 2:
            select_tools.show_tickets()
    # 退票 3
        elif action == 3:
            select_tools.checkout_tickets(select_tools.select_tickes())


    # 返回主页面 0
        else:
            print('欢迎您再次使用影院订票系统，祝您观影愉快！！！')
            break
    else:
        print('您输入有误，请重新输入')