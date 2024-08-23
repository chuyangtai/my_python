#Timeline时间线
from pyecharts.charts import Bar,Timeline
from pyecharts import options
from pyecharts.globals import ThemeType #主题类型

bar1 = Bar()
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar1.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])


bar2 = Bar()
bar2.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar2.add_yaxis("商家A", [15, 30, 36, 10, 275, 90])


bar3 = Bar()
bar3.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar3.add_yaxis("商家A", [25, 20, 56, 110, 175, 100])


#构建时间线对象，多个点
timeline = Timeline(
    #字典
    {'theme': ThemeType.LIGHT}
)
timeline.add(bar1, "1月")
timeline.add(bar2, "2月")
timeline.add(bar3, "3月")
#设置时间线轴的样式
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
    is_inverse=False
)

timeline.render('./charts_html/charts_timeline.html')

