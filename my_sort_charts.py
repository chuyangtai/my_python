#列表对象的sort方法，sort(key-排序函数-指定根据什么排序,reverse升序|降序)
from pyecharts.charts import Bar,Timeline
from pyecharts import options
from pyecharts.globals import ThemeType #主题类型
my_list=[['a',33],['b',42],['c',11],['d',22],['e',55],['f',66],['g',77],['h',88],['i',99],['j',10]];

bar = Bar()
xData=[]
yData=[]
for e in my_list:
    xData.append(e[0])
    yData.append(e[1])
bar.add_xaxis(xData)
bar.add_yaxis("柱状图数据",yData)
bar.reversal_axis() #反转x轴数据
bar.set_global_opts(title_opts=options.TitleOpts(title="排序图表数据"))

my_list=[['a',33],['b',42],['c',11],['d',22],['e',55],['f',66],['g',77],['h',88],['i',99],['j',10]];
#简化用匿名函数传入,实现
my_list.sort(key=lambda elem:elem[1],reverse=False) #升序
print(my_list)
bar1 = Bar()
xData=[]
yData=[]
for e in my_list:
    xData.append(e[0])
    yData.append(e[1])
bar1.add_xaxis(xData)
bar1.add_yaxis("柱状图数据",yData)
bar1.reversal_axis() #反转x轴数据
bar1.set_global_opts(title_opts=options.TitleOpts(title="排序图表数据-升"))
def sort_key(elem):
    return elem[1]
my_list.sort(key=sort_key,reverse=True) #降序
print(my_list)

bar2 = Bar()
xData=[]
yData=[]
for e in my_list:
    xData.append(e[0])
    yData.append(e[1])
bar2.add_xaxis(xData)
bar2.add_yaxis("柱状图数据",yData)
bar2.reversal_axis() #反转x轴数据
bar1.set_global_opts(title_opts=options.TitleOpts(title="排序图表数据-降"))


#构建时间线对象，多个点
timeline = Timeline(
    #字典
    {'theme': ThemeType.LIGHT}
)
timeline.add(bar, "1月")
timeline.add(bar1, "升序")
timeline.add(bar2, "降序")
#设置时间线轴的样式
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False,
    is_inverse=True,
)

timeline.render('./charts_html/charts_sort.html')

