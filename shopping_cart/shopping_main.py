from shopping_cart import shopping

print({'名称': '鸡蛋',  '价格': 5,'库存': 100},
      {'名称': '面包', '价格': 2, '库存': 50},
      {'名称': '牛奶', '价格': 6, '库存': 30})

list2 = []
while True:
    goods_name = input('请输入商品名称：')
    goods_num = input('请输入购买商品的数量：')
    shopping.name(goods_name.strip())
    list2.append(goods_name)
    print(list2)




