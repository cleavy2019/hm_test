def input_password():
    # 1.用户输入密码
    pwd = input("请输入密码：")
    # 2.如果密码长度>= 8 ，返回输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.提示用户密码输入长度不足
    print("密码长度不足")
        # 1. 创建异常对象 —— 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不足……")
        # 2.主动抛出异常
    raise ex



# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)