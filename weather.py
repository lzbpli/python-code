#-*-coding:gbk -*-
import urllib2
import json
from city import city

# cityname = ram_input('������Ǹ����е�����\n')
cityname = raw_input('������ĸ����е�������\n')
citycode = city.get(cityname)

if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    concent = urllib2.urlopen(url).read()
    print concent
