def demo1():
    return (int(input("请输入整数：")))

def demo2():
    return demo1()

# print(demo2())

# a 异常

# 出现异常时，异常会向上传递给函数的调用方，直到找到异常的处理，如果没有处理，程序终止

# 利用异常的传递性，在主程序捕获异常

# 异常的传递--当 函数/方法 执行出现 异常，会将异常传递给 函数/方法 的调用一方
# 如果 传递到主程序，仍然 没有异常处理，程序才会被终止

try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)