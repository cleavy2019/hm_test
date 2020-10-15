'''购物车需求
1.用户自助选择购物商品
2.用户可以查看购物车的选择商品
3.用户可以选择去除购物车的商品
4.用户结账'''


list1 = {'名称': '鸡蛋','价格': 3, '库存': 100 }
print(list1)

list2 = []
while True:
    action = int(input('请输入您的操作：'))
    if action == 1:
        goodsname = input('请输入购买商品的名称：')
        goodsnum = input('请输入购买商品的数量：')
        list2.append(goodsname)
        # print(list1.get('库存')-int(goodsnum))
        list1['库存'] = 100 - int(goodsnum)
    if action == 2:
        print(list2)
    if action == 3:
        print(list1)













