dic = {"name": "zhangsan", "age": "25", "weight": "80"}
print(dic.values())
print(dic['name'])

str1 = "hello python"
# for char in str1:
#     print(char)
#
# print(str1[6])

str2 = str1.upper()
print(str2)

class Persion:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print("我的体重是%.2f" % self.weight)
    def eat(self):
        self.weight += 1
        print("我的体重是 %.2f" % self.weight)
xiaoming = Persion("小米", 78.0)

xiaoming.run()
xiaoming.eat()

