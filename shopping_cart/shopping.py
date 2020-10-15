goods_list = [{'名称': '鸡蛋',  '价格': 5,'库存': 100},
              {'名称': '面包', '价格': 2, '库存': 50},
              {'名称': '牛奶', '价格': 6, '库存': 30}]

shopping = []

def name(goods_name):
    """
    :param goodsname: 商品名称
    :return:
    """
    list1 = []

    for i in goods_list:
        list1.append(i.get('名称'))
    if goods_name in list1:
        print('购物车已为您添加【%s】' % goods_name)
    else:
        print('输入的商品暂未找到')























# class Goods:
#     def __init__(self, name, price, ku):
#         self.name = name
#         self.price = price
#         self.ku = ku
#
#     def name(self):
#         print(self.name)
#
#     def price(self):
#         return self.price
#
#     def ku(self):
#         print(self.ku)
#
# pg = Goods('苹果', '5', '100')
# print(pg.price)































