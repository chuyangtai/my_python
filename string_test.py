# python中字符串类型不能修改，必须要用新的字符串接收。属于数据容器
# 字符串，用下标索引访问单个字符
s = '视频的单片付费'
print(s[-1])

# replace,字符串的替换
s1=s.replace('视频','专辑')
print(f'原字符串：{s}')
print(f'新字符串：{s1}')

# split(分隔符，分割次数),分割字符串,返回数组
s2="支付订单,支付剧集,单片支付,全集付费"
s3=s2.split()
print(f'分割：{s3}')
s4=s2.split(',')
print(f'分割：{s4}')
s5=s2.split(',',2)
print(f'分割：{s5}')

# strip() 移除字符串头尾指定的字符（默认为空格或换行符），不能删除中间部分的字符
s6="   支付订单 支付剧集 单片支付/n全集付费/n/r   "
print(f'去除前：{s6}')

#默认去除的是首尾的的空格
s7=s6.strip()
print(f'去除后：{s7}')

# 字符序列为 12，去除字符串1和2
str = "123abcrunoob3211"
print (str.strip( '12' ))

# count 统计出现次数
print(str.count('1'))

# len 统计长度
print(len(str))

#while for循环可以对字符串进行遍历

