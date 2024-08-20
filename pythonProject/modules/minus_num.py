#自定义模块
def num(a,b):
    print(a-b)
#每个模块（Python 文件）都有一个特殊的内置属性 __name__
# 当一个模块作为主程序直接运行时，__name__ 的值被设置为 '__main__'。
# 当一个模块被另一个模块导入时，__name__ 的值被设置为模块的名称（不包含.py 扩展名）。
print(__name__)
if __name__=='__main__':
    num(2, 3)
# __all__ = ['function1', 'MyClass']指定导入模块的*代表哪些函数功能