class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍……" % self.name)

class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上玩耍" % self.name)


class Persion(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 愉快的玩耍" %(self.name, dog.name))

       # 让狗玩耍

        dog.game()
# 1. 创建狗类
# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")
# 2. 创建小明类
xiaoming = Persion("小明")
# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
