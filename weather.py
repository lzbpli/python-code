#-*-coding: GBK -*-
import urllib2
import json
from city import city

cityname = raw_input('������ĸ����е�������\n')
citycode = city.get(cityname)

if citycode:
	try:		
		url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
		concent = urllib2.urlopen(url).read()
		data = json.loads(concent)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (
			result['weather'],
			result['temp1'],
			result['temp2']
		)
		print str_temp
	except:
		print '��ѯʧ��'
else:
	print 'û�г���'