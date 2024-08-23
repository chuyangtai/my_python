# 类
import json


class St:
    #属性（成员变量）
    name = None
    gender = None
    age = None
    native_place = None
    nationality = None

    #行为（成员方法）,都要传入self，通过self访问到成员变量,形参跟在后面
    def say(self):
        print('我叫%s,今年%d岁，来自%s，我的国籍是%s' % (self.name, self.age, self.native_place, self.nationality))

    def eat(self, smg):
        print('我喜欢吃%s' % smg)


#创建一个对象，并赋值属性值
stu_1 = St()
stu_1.name = '张三'
stu_1.gender = '男'
stu_1.age = 20
stu_1.native_place = '北京'
stu_1.nationality = '中国'
#self不需要传参，是内部参数
stu_1.say()
stu_1.eat('火锅')

#str1和str2互不干扰，各玩各的
stu_2 = St()
stu_2.name = '张洁'
stu_2.gender = '女'
stu_2.age = 18
stu_2.native_place = '杭州'
stu_2.nationality = '中国'
stu_2.say()
stu_2.eat('饺子')


#类可以完美描述现实世界中的实物，类是设计图纸，对象才是实现活动的实体
#类是抽象的，对象是具体的
#类是对象的模板，对象是类的实例

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(400, 1000)  #频率，持续时间
        # winsound.Beep(400, 1000)
        # winsound.Beep(400, 1000)


#创建对象
clock_1 = Clock()
clock_1.id = '001'
clock_1.price = 1000
clock_1.ring()


#构造方法，名字为__init__，创建对象时自动调用，构建类对象时，会自动执行
#构造方法可以传参，赋值给成员变量
#构造方法必须有self参数，self代表类的对象
class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        # 私有成员变量，私有成员以两个下划线开头，不能被外部访问，但可在类内部被其他成员访问。
        self.__money = 0
        print('init')  #构造方法可以写任意代码，构建对象后不用调用，就自动执行

    # 私有成员方法，私有成员方法以两个下划线开头
    def __deposit(self):
        print(f'私有，{self.__money}')

    def say(self):
        print('我是%s' % self.name)
        if self.__money <= 0:  #私有成员变量只能在类内部访问，外部无法访问
            self.__deposit()
            print('余额不足')

    # 魔术方法，前面两个下划线，后面两个下划线
    def __str__(self):  #__str__方法是一个特殊的方法，用于定义对象的字符串表示形式。打印对象时，自动调用.
        #默认打印对象为内存地址，以下是自定义的对象打印形式
        return 'name:%s,age:%s' % (self.name, self.age)

    def __lt__(self, other):  # >、< 不支持=，other为对比的对象,通过age比较两个对象的大小，返回true或false。
        return self.age < other.age

    def __le__(self, other):  # >=、<= ，other为对比的对象,通过age比较两个对象的大小,返回true或false
        return self.age <= other.age

    def __eq__(self, other):  # == other为对比的对象,通过age比较两个对象是否相等,返回true或false
        return self.age == other.age


st1 = Student('1', '男', 18)  #构造方法可以写任意代码，构建对象后不用调用，就自动执行print('init')
st2 = Student('2', '男', 29)  #对象2
st3 = Student('3', '女', 29)  #对象3
print(st1)  #打印对象时，自动调用__str__方法
st1.say()

print(st1 < st2)  #lt比大小的功能
print(st1 > st2)
print(st2 <= st3)  #le比大小的功能
print(st2 >= st3)
print(st2 == st3)  #没写魔术方法，比较的是内存地址结果都是false,魔术方法可以比较某个属性得到true


#封装--将现实世界的事物描述为成程序中的类的一种思想
#私有成员变量和方法：
#程序内部调度一般是私有的，不能外部访问
#print(st1.__money)#私有成员变量，不能直接访问
#st1.__deposit()#私有成员方法，不能直接访问
class Phone:
    IMEI = None  #序列号
    producer = 'HM'  #产商
    __is5G = False  #5G状态,True/False

    def __check5G(self):
        if (self.__is5G):
            print('5G网络已开启')
        else:
            print('5G网络关闭,正在使用4G网路')

    def call_by_5G(self):
        self.__check5G()
        print('通话中...')


ph1 = Phone()
ph1.call_by_5G();


#继承
#在类定义时在类名后的括号中指定父类来实现,如果一个类有多个父类，可以在括号中以逗号分隔的方式列出多个父类，这被称为多重继承。
class Phone2024(Phone):  #Phone2024继承Phone,基于上一代手机修修改改，增加一些新的功能
    def face(self):
        print('人脸识别')


ph2 = Phone2024()
ph2.call_by_5G();


class NFCreader:  #NFC读卡器
    nfcType = '第5代'
    producer = 'HUAWEI'  # 产商

    def readNFC(self):
        print('NFC读取卡信息')

    def witerNFC(self):
        print('NFC写入卡信息')


class RemoteControl:  #遥控器
    producer = 'XIAOMI'  # 产商

    def turnOn(self):
        print('打开红外遥控器')

    def turnOff(self):
        print('关闭红外遥控器')


class MyPhone(Phone2024, NFCreader, RemoteControl):  #多重继承，拿来吧你
    pass;  #不能空着的时候，用来补全语法，用pass占位


mp = MyPhone()
print('原生调用-开始')
mp.call_by_5G()
print('原生调用-结束')
mp.readNFC()
mp.turnOn()
print(mp.producer)  #同名成员方法，按谁先继承，先继承的优先级最高，Phone2024的


#复写
# 重新写一遍就可以覆盖了,修改父级属性、方法，修改继承的父类方法
class MyChildPhone(Phone2024, NFCreader, RemoteControl):  #多重继承，自己改装
    producer = 'MYSELF'  # 产商

    # 升级父级的call_by_5G方法
    def call_by_5G(self):  #复写优化父级方法
        print('升级通话中...')
        print('保持省电，保持信号中...')
        super().call_by_5G()  #调用父级方法-1,super拿到父级，不用传self
        Phone2024.call_by_5G(self)  #调用父级方法-2，需要传self
        print(super().producer)  #调用父级属性
        print(Phone2024.producer)  #调用父级属性


mcp = MyChildPhone()
print(mcp.producer)  #复写了父类属性，但父类属性还在
mcp.call_by_5G()  #复写了父类方法，但父类属性还在


# 多态
# 将父类、子类、或其他不相干的类都有相同的方法时，用一个统一的接口方法集合起来，传入不同对象，产生不同的结果
class CallInterface(object):  # 把对象传入，调用接口，会调用对象类中定义的方法，每个类会有自己的核心方法。
    def call(self,obj):
        obj.call_by_5G()

c=CallInterface()
print('MyPhone用多态调用接口方法-开始')
c.call(mp)
print('MyPhone用多态调用接口方法-结束')
# 类型注解，提示值和参数的类型
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))

# 变量注解，无法一眼看出来类型的时候，需要注解
my_list: list = [1, 2, 3]
my_list2: list[int] = [1, 2, 3]

# 注释注解,会变亮
my_list3 = [1, 2, 3]  # type: list[int]

# json转为字典类型
my_num = json.loads('{"a":1,"b":2}')  # type: dict[str,int]


# 函数注解 , ->返回值类型
def add(a: int, b: int) -> int:
    return a + b


# 返回值为none表示没有返回值或者返回none
def process_list(lst: list[int]) -> None:
    for item in lst:
        print(item)


process_list(['a', 'b', 'c'])  # 传错了不会报错

# 联合类型
from typing import Union

my_u: int | str = 1  # 联合类型，可以是int或者str
my_u1: list[Union[int, str]] = [1, 2, 'a']  # 联合列表类型，可以是int或者str

