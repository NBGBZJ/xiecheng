# from IP_LIST import IP_list
import requests
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://www.flycua.com/otabooking/flight-search!doFlightSearch.shtml?rand='
#url = 'http://ip.chinaz.com/'
randoms = random.uniform(0, 1)
url = url + '%.17f' % randoms
data = 'searchCond={"tripType":"OW","adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","sortType":"a","segmentList":[{"deptCd":"SZX","arrCd":"NAY","deptDt":"2015-12-05","deptCityCode":"","arrCityCode":""}],"sortExec":"a","page":"0"}'
headers ={'Origin': 'http://www.flycua.com',
          'Connection': 'keep-alive',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Referer': 'http://www.flycua.com/flight2014/SYX-NAY-151111_CNY.html',
          'X-Requested-With': 'XMLHttpRequest',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Host': 'www.flycua.com',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}

#IP_list = [{u'http': u'http://183.12.204.116:8090'}, {u'http': u'http://221.221.220.165:8090'}, {u'http': u'http://118.170.41.246:8888'}, {u'http': u'http://118.170.41.246:8888'}]
#proxies = random.choice(IP_list)
proxies = {'http': 'http://lijunqiang316027648:18838733354@104.217.235.133:8888'}
print(url)
print(proxies)

r = requests.post(url=url, data=data, headers=headers,proxies=proxies)
print(r.text)
