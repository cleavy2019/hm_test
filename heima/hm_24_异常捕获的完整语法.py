# try 完整语法
'''
try:
    # 尝试执行的代码
    pass
except 错误类型1:
    # 针对错误类型1，对应的代码处理
    pass
except 错误类型2:
    # 针对错误类型2，对应的代码处理
    pass
except 错误类型3:
    # 针对错误类型2，对应的代码处理
    pass
except Exception as result:
    # 打印未知的错误信息
    print(result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行")
'''


try:
    # 提示用户输入一个整数

    num = int(input("请输入一个整数："))

    # 使用8除以用户输入的整数并且输出

    result = 8 / num

    print(result)

except ValueError:
    print("请输入正确的整数")

except Exception as result:
    print("未知错误 %s" % result)

else:
    print("尝试成功")
finally:
    print("无论是否成功，都会被执行")

print("-" * 50)