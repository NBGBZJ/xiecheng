# -*- coding:utf-8 -*-

import requests
import random
import json
from datetime import datetime
from datetime import timedelta
import time
import socket
from class_xiecheng import home
from my_log import  log_set
import sys
import multiprocessing
reload(sys)
sys.setdefaultencoding('utf-8')
from IP_LIST import IP_list
#from fb_xc import feiba_data


class spider:
    def __init__(self, tripType = 'OW', adtCount=1, chdCount=0, infCount=0, currency='CNY',sortType='a',
                 deptCd='', arrCd= '', deptDt='', deptCityCode = '',arrCityCode='',sortExec='a', page=0):

        self.deptCd = deptCd
        self.arrCd = arrCd
        self.deptDt = deptDt
        self.deptCityCode = deptCityCode
        self.arrCityCode = arrCityCode

        self.url = 'http://www.flycua.com/otabooking/flight-search!doFlightSearch.shtml?rand='
        #self.url = "http://114.215.123.231:32771/"

        self.data = 'searchCond={"tripType":"%s","adtCount":%s,"chdCount":%s,"infCount":%s,"currency":"%s","sortType":"%s",\
"segmentList":[{"deptCd":"%s","arrCd":"%s","deptDt":"%s","deptCityCode":"%s","arrCityCode":"%s"}],' \
                    '"sortExec":"a","page":"0"}' % (tripType,adtCount,chdCount,infCount,currency,sortType,
                                                    deptCd,arrCd,deptDt,deptCityCode ,arrCityCode)
        self.url_page = ('http://www.flycua.com/flight2014/%s-%s-'+deptDt[2:].replace('-','')+'_CNY.html')%(self.deptCd,self.arrCd)
        self.headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
                    'Accept-Encoding':'gzip, deflate',
                    'Accept-Language':'zh-CN,zh;q=0.8',
                    'Connection':'keep-alive',
                    #'Content-Length':'235',delete is ok
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    #'Cookie':self.get_cookies(),delete is ok
                    'Host':'www.flycua.com',
                    'Origin':'http://www.flycua.com',
                    'Referer':self.url_page,
                    'User-Agent': "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
                    'X-Requested-With':'XMLHttpRequest'
                   }

    def do_work(self):
        # print(self.deptDt)
        timeout = 10
        socket.setdefaulttimeout(timeout)
        randoms = random.uniform(0, 1)
        url = self.url + '%.17f' % randoms
        ############# proxies##########
        #prox_list = [{'http': 'http://test:hktest@103.27.125.250:6666'}]
        proxies = random.choice(IP_list)
       # print(proxies)

        ###################

        try:
            # log_set(name='lianhe',msg='#################################################')
            log_set(name='class_xiecheng',msg='验证网站'+str(self.url_page))
            print(self.url_page)
            #print(url)
            # print(self.headers)
            print(proxies)
            time.sleep(5)
            r = requests.post(url=url, data=self.data, headers=self.headers,proxies=proxies, timeout=10)
            
            cont = r.content
            print(cont)

            if len(cont) > 2500:
                print('yes')
                return cont
            else:
                print('sessionId� fail')
                # log_set(name='lianhe', msg='[lianhe]sessionId获取失败，参数错误，%s,%s,%s'%(self.url_page, self.deptDt,proxies))
                return ''

        except Exception as e:
             print('网络请求问题')
             log_set(name='lianhe', msg='lianhe]i,cant online:%s,%s,%s'%(self.url_page, self.deptDt,proxies))
             return ''

def deal_data(json_date):
    info_list = list()
    info =dict()
    #print(json_date)
    try:
        json_date = json.loads(json_date, encoding='utf-8')
        # print(json_date)
        allFlight = json_date['airResultDto']['productUnits']
        for i in range(0, len(allFlight)):
                print(i)
                hlq_str = 'SVTZU'
                if allFlight[i]['productInfo']['productCode'] == 'HLY':
                    #print('HLYhlYHLy',allFlight[i]['productInfo']['productCode'])
                    print('get HLY_NUM='+str(len(allFlight)))
                    for k in range(0, len(allFlight[i]['oriDestOption'])):
                        for m in range(0,len(allFlight[i]['oriDestOption'][k]['flights'])):
                            if allFlight[i]['oriDestOption'][k]['flights'][m]['bookingClassAvail']['cabinCode'] in hlq_str:
                                hangban = (allFlight[i]['oriDestOption'][k]['flights'][m]['marketingAirline']['flightNumber'])
                                print('hangban'+hangban)
                                yupiao = (allFlight[i]['oriDestOption'][k]['flights'][m]['bookingClassAvail']['cabinStatusCode'])
                                print(yupiao)
                    for t in range(0,len(allFlight[i]['fareInfoView'])):

                       the_hlq_str = (allFlight[i]['fareInfoView'][t]['fareBasisCode']).encode('utf-8')
         #              print('hlq_str is :',the_hlq_str )
          #             print(type(the_hlq_str))
                       if the_hlq_str[0] in hlq_str:
                            hly = (allFlight[i]['fareInfoView'][t]['fare']['fdPrice'])
                            if float(hly) >8:
                                info[hangban] = (yupiao, hly)
                                print('OKOOOKOKinfo',info)
                                info_list.append(info)



             #                   print('8元抢票')
            #                    # log_set(name='lianhe', msg='[lianhe]8元抢票')
        print('info_list',info_list)
        return info_list
    except:
        return info_list

def feiba_main(deptCd, arrCd, start_day=0, over_day=10):
    #q = Queue(connection=Redis())
    try:
        start_day = int(start_day)
        days = int(over_day) #延迟天数
        deptCd = deptCd.upper()
        arrCd = arrCd.upper()
    except:
        return {'code':1}
    # print(start_day, days, deptCd, arrCd)
    now =datetime.now()
    for s in range(start_day, days):
        a = timedelta(days=s)
        YearMonthDate = (str(now+a)[:10])
        do_work = spider(deptCd=deptCd, arrCd=arrCd, deptDt=YearMonthDate)
        spy_data = do_work.do_work() #获得str数据
        if len(spy_data)>2000:
            """有取到有效信息"""
            info_list = deal_data(spy_data)
            print('all hyl is',(info_list))
            ## log_set(name='lianhe', msg='[lianhe]all hyl is'+str(info_list))

            for info in info_list:
               #one_info=dict()
             #  print(YearMonthDate+'//飞机航班号：'+ info+'//'+'剩余票数：'+ (info_list[info][0]) + '//欢乐抢单程单价:'+info_list[info][1])
              # log_set(name='lianhe', msg='lianhe:'+YearMonthDate+',fight_no：'+ info+':'+'invent：'+ (info_list[info][0]) + ':feiba_price:'+info_list[info][1])
               print('#############去做对比工作和投放#############')
               #one_info[info] = info_list[info]
               #log_set(name='duibi', msg='[lianhe]'+YearMonthDate+'//飞机航班号：'+ info+'//'+'剩余票数：'+ (info_list[info][0]) + '//欢乐抢单程单价:'+info_list[info][1]+deptCd+arrCd)
               print('YYYYYYYYYYYYYYY')
               #print(one_info)
               p = multiprocessing.Process(target=home, args=(YearMonthDate, deptCd, arrCd, info, 0))
               p.start()

        if not len(spy_data):
            print('已经没有欢乐抢机票了')
            log_set(name='lianhe', msg='[lianhe]it have not invent')
            #return {'code':1}
            #TO 下次再爬，单独爬某一天方法##############

    #return 'will down'


if __name__ == '__main__':
    """   DSN-CSX """
    feiba_main(over_day=10, start_day=0, deptCd="NAY",arrCd="SZX")





