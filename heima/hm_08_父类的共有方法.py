class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的共有方法 %d" % self.__num2)
        self.__test()

class B(A):

    def demo(self):

        # 1. 访问父类的私有属性
        # print("访问父类的私有属性 %d " % self.__num2)
        # 2. 调用父类的私有方法
        # self.__test()
        # 3.访问父类的共有属性
        print("子类方法 %d" % self.num1)

        # 4.调用父类的共有方法
        self.test()

        pass

# 创建一个子类对象
b = B()

b.demo()
# 在外界访问父类的公有属性或调用共有方法
print(b.num1)
b.demo()

# 在外界不能直接访问对象的私有属性或调用私有方法
# print(b.__num2)
# b.__test()


