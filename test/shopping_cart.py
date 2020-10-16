class ShopingCart(object):
    # 购物车为空
    shopping_cart_list = []

    def __init__(self, goods_name, goods_price):
        self.goods_name = goods_name
        self.goods_price = goods_price

    # 给购物车添加商品
    def add_goods(self):
        self.shopping_cart_list.append(self.goods_name)
        print("购物车商品为：%s" % self.goods_name)

    # 给购物车去除商品
    def del_goods(self):
        self.shopping_cart_list.remove(self.goods_name)
        print("去除了购物车里的商品%s" % self.goods_name)

    # 购物车去结账
    def order_goods(self):
        price = int(self.goods_price) * 20
        print("商品价格为 %d" % price)


shopping_cart = ShopingCart("茶叶", 1.0)
shopping_cart.add_goods()
shopping_cart.del_goods()
shopping_cart.order_goods()

shopping_cart = ShopingCart("jidan", 3)
shopping_cart.add_goods()
shopping_cart.del_goods()
