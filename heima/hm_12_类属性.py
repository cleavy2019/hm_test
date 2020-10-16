class Tool(object):

    # 使用赋值语句记录创建了多少个类对象
    count = 0

    def __init__(self, name):
        self.name = name
        # 类属性值 +1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("榔头")
tool2 = Tool("铁锹")
tool3 = Tool("锄头")

# 输出工具对象的总数
print(Tool.count)