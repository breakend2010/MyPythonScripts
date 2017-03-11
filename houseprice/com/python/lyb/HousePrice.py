#!/usr/bin/python
# coding=utf-8
import urllib2
import json
import time

from matplotlib.pyplot import *
chengdu="%u6210%u90FD"  #成都的url编码
hangzhou="%u4E0A%u6D77" #杭州的url编码
shanghai="%u4E0A%u6D77" #上海的url编码
beijing="%u5317%u4EAC" #北京
shenzhen="%u6DF1%u5733" #深圳

print "开始获取数据..."

#todo 只需要改以下两个参数
year=12  #设定获取多少年的数据，一般城市最大为10年,上海北京有11年的
city=shenzhen
city_title=u"深圳"

url="http://fangjia.fang.com/pinggu/ajax/chartajax.aspx?dataType=3&city="+city+"&Class=defaultnew&year="+str(year)
data=urllib2.urlopen(url)
result = data.read()
end = result.index("&") #结果的结尾位置,&后面为当前房价
result = result[1:end-2] #[],[],[]格式
values = result.split("],") #分隔成数组
disk = {};
ISOTIMEFORMAT='%Y-%m'
times = ()
prices = ()
xticks_tags = ()
for value in values:
    temp = value[1:len(value)].split(",")
    date = time.strftime(ISOTIMEFORMAT, time.localtime(float(temp[0]) / 1000))  # 将时间戳转换成日期
    times += (float(temp[0]),)
    prices += (temp[1],)
    xticks_tags += (date,)
print "disk已转码完成..."

xticks_tags_value =()
xticks_tags_tag = ()
#todo 标记方案1
index = 0;
for tags in xticks_tags:
    if("-12" in tags):
        xticks_tags_value += (times[index],);
        xticks_tags_tag += (tags,)
        index=index+1
    else:
        index=index+1

#todo 方案二
#以当前月份为基准，每隔12个月打个标签
# xticks_tags_value = times[::12]# 以12为步长的话就是一年取一个数据做标记
# xticks_tags_tag = xticks_tags[::12] #

#
plot(times,prices)
#axis([-4, 4, -0.5, 8])
xticks(xticks_tags_value,xticks_tags_tag)
xlabel(u'时间')
ylabel(u'二手房均价')
title(city_title+u'近十年房价走势', fontsize=16)
grid(True)
# show()
# savefig(u"杭州市近十年房价走势.jpg",dpi=100)
print "done"
