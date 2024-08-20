#它指的是一系列有序排列的元素集合。这些元素可以是不同的数据类型，但它们在序列中的位置是有序的，即每个元素都有一个特定的索引（或位置）
#列表（List）、元组（Tuple）和字符串（String）属于内置序列
# 切片，sequence[start:stop:step]  与js中的slice()方式类似，不包括最后一个
l0=['综艺', '少儿', '影视剧', '纪录片']
#从头到尾
l1=l0[:]
#反转
lr=l0[::-1]
print(lr)
#取出从0到2的子数组，不包含第2个
l2=l0[0:2]
# 步长是2时，中间隔一个
l3=l0[0:4:2]
# 步长为负数，从后往前取，-1是最后一位
l4=l0[-1:-2:-1]
l5=l0[-1:-5:-2]
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

# 集合
# 集合，自带去重功能，不支持元素的重复，用{}表示，类型为set
# 集合没有顺序，不支持下标索引，取出为随机
c={2,3,5}
print(c)
print(type(c))

# 会自动去重
c1={2,1,2,2,3,5}
print(c1)
c2=set()
print(c2)

#add增
c2.add('会员')
c2.add('首开')
c2.add('礼包')
c2.add('抽奖')
print(c2)

c2.remove('首开')
print(c2)

#pop 随机删除
ele=c2.pop()
print(c2)

#clear
c2.clear()
print(c2)

#difference 差集
s1={'会员', '抽奖', '礼包', '首开','开卡礼'}
s2={'会员', '抽奖', '礼包', '首开','规则'}
s3=s1.difference(s2)
s4=s2.difference(s1)
print(s3)
print(s4)


#difference_update 消除差集
s1.difference_update(s2)
print(f'消除后{s1}')

#union 合并集合
s1={'会员', '抽奖', '礼包', '首开','开卡礼'}
s3=s1.union(s2)
print(f'合并后{s3}')

#len 去重个数
print(f'去重个数{len(s3)}')

#循环遍历不能用while循环，只能用for循环
for i in s3:
    print(i)

#字典dict
# 用{k:v},通过key找到对应的value,不允许key重复
d={"月度会员":1,'季度会员':16,'年度会员':48}
d1=dict()
print(type(d))
print(d)
print(d1)

#重复的后面会覆盖前面的
#没有下标索引
print(d["月度会员"])

#key可以是任何类型但不可是字典，value可以是任意类型
d2={
    'amount': "34.666",
    'consumerNickName': "姓名",
    'durationConfig': {
        'unit': "3",
        'value': "333",
    },
    'gmtCreate': "",
    'paySuccessTime': "2024-3-4",
    'paymentMethod': "WECHAT_PAY",
    'mediaName': '标题'
}
print(d2)
print(d2['durationConfig']['value'])

#新增元素，直接定义key,value
d2['payList']=[2,3]
print(d2)

#pop[key]删除
d2.pop('amount')
print(d2)

#keys
print(d2.keys())

#字典不能用while循环,用for-in循环
for key in d2:
    print(f'打印{key}')
    print(d2[key])

#列表、元组、字符串---序列类型，支持下标索引
#集合、字典---非序列类型，不支持下标索引
#max\min
print(f'最大值{max(s1)}')
print(max(c1))
print(max(d2))
print(min(s1))
print(min(c1))
print(min(d2))

#强转 set转集合、list转列表、
#字典转列表,只剩下key
st='只剩下key'
print(f'元组{tuple(s1)}')
print(f'元组{tuple(st)}')
print(f'元组{tuple(d)}')
print(f'集合{set(s1)}')
print(f'集合{set(st)}')
print(f'集合{set(d)}')

my_tuple = (1, 2, 3, 4, 5)
# 使用list()函数将元组转换成列表
my_list = list(my_tuple)
print(my_list)  # 输出: [1, 2, 3, 4, 5]
#'list' object is not callable是因为定义了一个名为list的变量，list不再是指向内置的list()函数

#其它类型，不能转成字典类型

#排序 sorted
c1={2,1,2,2,3,5}
print(f'集合{sorted(s1)}')
print(f'集合{sorted(st)}')
print(f'集合{sorted(c1)}')

#反向排序 sorted
c1={2,1,2,2,3,5}
print(f'集合{sorted(s1,reverse=True)}')
print(f'集合{sorted(st,reverse=True)}')
print(f'集合{sorted(c1,reverse=True)}')

#字符串排序按照字符对应的asic码的数值比较,按位比较，ab比a大
print('abd'>'abc')
#大写字母和小写字母的asic码也是不一样的
print('paySuccessTime'>'paymentMethod')

