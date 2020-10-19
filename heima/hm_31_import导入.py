# 如果两个模块 中存在同名函数，那么 后导入模块的函数会覆盖掉先导入的函数
from heima.hm_27_测试模块1 import say_hello
from heima.hm_28_测试模块2 import say_hello

say_hello()