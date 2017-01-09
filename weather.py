#-*-coding:gbk -*-
import urllib2
import json
from city import city

# cityname = ram_input('你想查那个城市的天气\n')
cityname = raw_input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)

if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    concent = urllib2.urlopen(url).read()
    print concent
