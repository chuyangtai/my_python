#通过翻译成二进制，就可以完成对文件的操作，一般用UTF-8，各种语言都支持，比较通用
#使用 open() 函数打开文件，并指定打开模式为写入模式（'w'）
#读取模式 r，将文件一行一行打印出来
#file为一个类被实例化后的实例对象，有一系列可供使用的方法
#open(name.mode,encoding),mode-r/a/w
#with open as,该方法会自动关闭文件，不用close手动关闭
with open('./files/info.txt', 'r') as file:
    for line in file:
        print(line, end='') #end=''代表不换行
f=open("E:/py/pythonProject/files/w.txt",'r',encoding="gbk")
print(f"绝对路径打开文件:{f.read()}")
print(f"文件结束")
#写入模式 w,替换原来是内容
with open('./files/w.txt', 'w') as file:
    file.write('这是要写入文件的内容2。\n')
    file.write('这是新的一行内容2。')

#追加模式 a,在文末尾添加
with open('./files/w.txt', 'a') as file:
    file.write('这是要写入文件的内容111。\n')
    file.write('这是新的一行内容111。')

#read   读取全部
# readline 读取一行
# readlines 读取所有行
#file.read() 会读取整个文件的内容并返回一个字符串
with open('./files/w.txt', 'r') as file:
    content = file.read()
    print(content)

#读取字节数
with open('./files/info.txt', 'r') as file:
    content = file.read(10)
    print(f'读取10个字节的结果:{content}')
    afterContent=file.read(20)
    #细节：多个read会接力往后读取
    print(f'读取20个字节的结果:{afterContent}')
    lines = file.readlines()
    print(f'读取剩余的:{afterContent}')

#readlines() 读取文件的全部行到一个列表对象中，每一行是列表的一个元素
# 注意，readlines() 会将所有行一次性读入内存，对于非常大的文件可能不太合适。
with open('./files/w.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
#for循环读取文件，for-in文件对象
for line in open("./files/w.txt","r"):
    print(line)

#不存在这个文件时，生成一个文件，并写入
with open('./files/new.txt', 'w') as file:
    #反斜杠n,换行
   file.write('新建了一个文件并写入。\n')
   file.write('这是新的一行内容。')

#使用os模块创建空文件
import os
file_path = './files/os_new.txt'
os.open(file_path, os.O_CREAT)

#使用pathlib模块创建文件，pathlib是 Python 3.4 及以上版本中用于处理文件路径的模块：
from pathlib import Path
file_path = Path('./files/pathlib_new.txt')
file_path.touch()

#close()关闭文件，不关闭占程序内存，且文件会被占用
#flush()内容刷新，把内容写入文件硬盘中。close内置了flush的功能

#统计有几个the单词
with open("./files/words.txt","r") as f:
    count=0
    words=f.read()
    wordsS=words.split(' ')
    #直接用cuont函数统计
    print(wordsS.count("the"))
    #虽然用循环也可以
    for w in wordsS:
        if w=="the":
            count+=1
    print(count)


#筛选正式的消费记录
#这里errors='replace' 会将无法解码的字符替换为一个特殊的占位符（如 ?），以避免解码错误导致程序崩溃。
f=open('./files/records.txt','r',encoding='utf-8',errors='replace')
fw=open('./files/records.txt.bak','w',encoding='utf-8',errors='replace')
for eachLine in f:
    line=eachLine.strip()#去掉前后空格、换行
    print(eachLine)
    if line.split(',')[4]=='测试':
        continue #跳过本次，进入下一次循环
    fw.write(line)
    fw.write('\n')
f.close
fw.close

#捕获异常try-except
try:
    open('d.txt','r')#打开一个不存在的文件，会报错
except Exception as e:
    open('./files/yichang.txt', 'w')
    print(e)
#捕获 指定类型的异常
try:
    print(name)
except NameError as e: #指定只捕获未命名的异常
    print('出现了变量未定义的异常')
    print(e)
#捕获多个类型异常
try:
    print(1/0)
    print(name)
except (NameError,ZeroDivisionError) as e: #指定只捕获未命名的异常
    print('捕获多种异常')
    print(e)



#没有异常，执行的代码，else
try:
    print(123)
except (NameError,ZeroDivisionError) as e: #指定只捕获未命名的异常
    print('捕获多种异常')
    print(e)
else:
    print('没有出现异常')
#finally无论有没有异常都执行
try:
   f= open('d2.txt','r')#打开一个不存在的文件，会报错
except Exception as e:
    print(e)
    f= open('./files/yichang.txt', 'w')
finally:
    print("有没有异常我都执行")
    f.close();

#异常的传递：异常会按照函数调用的层次依次向上传递，从最内层的函数开始，直到找到能够处理该异常的 try...except 语句为止。
#如果顶层也没有相应的异常处理程序，程序将会终止并显示异常信息。
def fun1():
    a=1/0
    print("fun1执行")

def fun2():
    fun1()
    print("fun2执行")
#从fun1传给fun2，再传给try中，被捕获了，因此在最顶级的地方捕获异常就行。
try:
    fun2()
except Exception as e:
    print('调用了fun2后：',e)












