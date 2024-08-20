# 数据容器，数组
name_list = ['张三', '李四', '王五', True, 666, [1, 2, 3], '1']
print(name_list)
print(type(name_list))
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
i = name_list.index('王五')
print(f'王五的位置{i}')
# 改
name_list[2] = '修改'
print(name_list)
# 增
name_list.insert(1, '增加')
print(name_list)

# 追加单个
name_list.append('追加')
print(name_list)

# 追加数组，连接
nList = [1, 2, 3, '追加了整个数组']
name_list.extend(nList)
print(name_list)

# 删除del
del name_list[0]
element = name_list.pop(0)
print('删了两次后：', name_list)

# pop返回该删除元素
print('pop能获得删除的元素是：', element)

# remove移除某个元素，找到的第一个
name_list.remove("1")
print(name_list)

# clear清空列表
my_list = name_list
my_list.clear()
print(my_list)
print(name_list)

n_list = ['张三', '李四', '王五', True, 666, [1, 2, 3], '1']

# len列表长度
l = len(n_list)
print(l)

# count统计数量
count = n_list.count(1)
print(count)


# 定义函数
def list_while_function():
    my_list = ['支付失败', '未支付', '已支付', '支付成功']
    index = 0
    while index < len(my_list):
        print(f'列表的元素：{my_list[index]}', )
        index += 1


# 调用函数
list_while_function()


# 定义函数
def list_for_function():
    my_list = ['支付失败', '未支付', '已支付', '支付成功']
    #i是临时变量
    for i in my_list:
        print(f'列表的元素：{i}', )


# 调用函数
list_for_function()

# tuple元组，唯一的区别是元组的数组不能被篡改，用()定义，元素是可以重复的
t = ()
num = (1,)
content = tuple(('综艺', '少儿', '影视剧', '纪录片'))
print(type(t))
print(type(content))

# 嵌套的元组
t1=((1,2),2,3,4,5,6,7,8,9,8,6,5,3,1)
print(t1)

# 下标取元素与数组一样,count,len，while,for都能用,修改数组的函数不可用
print(content[0])
print(content.index('影视剧'))
print(t1.count(6))
print(len(t1))
i=0
while i<len(content):
    print(f"视频的分类：{content[i]}")
    i+=1

# 但是，如果元组中有数组元素，该数组元素的内容是可以修改的
type=(['综艺', '少儿', '影视剧', '纪录片'],t1)
print(type)
type[0][0]='奔跑吧'
print(type)





