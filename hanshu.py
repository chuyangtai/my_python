#函数返回多个值，用多个变量按顺序接收
def get_person_info():
    # 返回一个包含多个值的元组
    return "John", 30, "New York"

# 接收全部返回值为一个元组
person_info = get_person_info()
print(person_info)  # 输出: ('John', 30, 'New York')

# 或者，直接解包到多个变量中
name, age, city = get_person_info()
print(name)  # 输出: John
print(age)  # 输出: 30
print(city)  # 输出: New York


#关键字传参，greeting默认值为"Hello"，默认值设置需要放在最后。
def greet(name, greeting="首开会员"):
    print(f"{greeting}, {name}!")

#位置传参，按传递的位置匹配
greet("Alice")  # 输出: Hello, Alice!
greet("Bob", "购买过了")  # 输出: Hi, Bob!

#关键字传参，顺序无所谓，按关键字匹配，关键字参数必须放在位置参数的后面，放前面会报错。默认值设置需要放在最后。
greet(name="Alice")  # 输出: Hello, Alice!
greet(greeting="购买过了", name="Charlie")  # 输出: Hi, Charlie!
#混用
greet("混用",greeting="购买过了")

#位置不定长参数，星号*，返回一个元组
def noLongerTuple(*agrs):
    print(f"{agrs},类型是{type(agrs)}")
noLongerTuple("混用","购买过了")

#关键字不定长参数,两个星号**，满足key-value,返回一个数据字典。
def noLongerDict(**kwagrs):
    print(f"{kwagrs},类型是{type(kwagrs)}")
noLongerDict(name="我的海报",type="支持视频展示")

#函数作为参数传递，计算逻辑的传递
def compute(x,y):
    return x+y
def functionParam(compute):
    sum=compute(10,20)
    print(f"{sum},函数的类型为{type(compute)}")

functionParam(compute)

#简写,lambda匿名函数，可以直接省略return,一行代码函数，不能写多行
def functionParam2(compute):
    sum=compute(1,2)
    print(f"{sum},函数的类型为{type(compute)}")
functionParam2(lambda x,y:x+y)



