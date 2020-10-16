class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息：")

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史最高分 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦……" % self.player_name)


# 查看游戏的帮助信息
Game.show_help()

# 查看游戏历史最高分
Game.show_top_score()

# 开启游戏

game = Game("小明")
game.start_game()




