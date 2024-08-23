#模块就是一个py文件，提供了各种各样的类、函数、变量
#----用import导入
#import time
#程序睡眠5秒，暂停5秒执行
#time.sleep(5)

#----导入指定模块
# print('暂停5秒执行')
# from time import sleep
# sleep(1)
# print('暂停1秒执行')

#----导入所有的模块
# from time import *
# sleep(1)
# print('暂停1秒执行')

#----as别名
# import time as t
# t.sleep(1)
# print('暂停1秒执行')

#----as别名
# from time import sleep as sl
# sl(1)
# print('暂停1秒执行')

#自定义模块，模块名称就是文件名称，导入plus_num.py中的方法
# import sys
# sys.path.append('./my_modules')
# from plus_num import num
# from minus_num import num   #同名函数后面的覆盖前面的
# num(1,3)
#同名函数，后面的会覆盖前面的，一般被覆盖的会变灰。

#py包是一个文件夹，包含一堆py文件，还有__init__.py标识当前文件夹为包
#通过包名.模块名.方法

import package.module_one as m
m.infoPrintOne()
