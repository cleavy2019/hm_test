class Tool(object):

    # 使用赋值语句记录创建了多少个类对象
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 类属性值 +1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")

# 调用类方法
Tool.show_tool_count()
