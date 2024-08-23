# -*- coding: utf-8 -*-
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
#外面是list数组，里面是一个个元组
data=[
    ("北京市", 100),
    ("上海市", 200),
    ("广州市", 300),
    ("深圳市", 400),
    ("重庆市", 500),
    ("天津市", 600),
    ("河北省", 700),
    ("山西省", 800),
]
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True, #是否为分段型
        pieces= [
            {'min':1,'max':100, 'label':'低', 'color':'#FFA800'},
            {'min':101,'max':200, 'label':'中', 'color':'#FFA500'},
            {'min':201,'max':300, 'label':'高', 'color':'#FFFF00'}
        ]
    )
)
map.add("1", data, "china")#china这里，河南省就写河南
map.render('./charts_html/charts_map.html')


