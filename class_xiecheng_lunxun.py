# -*- coding:utf-8 -*-
import requests
import re
import hashlib
import uuid
from datetime import datetime
import sys
from my_log import log_set
from py_db import get2_id_from_info, get2_pri_from_info
reload(sys)
sys.setdefaultencoding('utf-8')
from class_xiecheng_delete import del_work
from class_xiechang_fix2 import fix_work

class DoXC:
    def __init__(self,yearDate,DepartPort,ArrivePort,tag):

        self.name = "政策管理"
        self.psw = hashlib.md5('政策管理#a1234567').hexdigest().upper()
        self.id = uuid.uuid1()
        self.url = 'http://exchdata.ctrip.com/Flight-Proxy-TradeQuickAPI/api/xml/LowPricePolicyList'
        self.yearDate = yearDate
        self.DepartPort = DepartPort
        self.ArrivePort = ArrivePort
        self.tag = tag
       
        #<?xml version="1.0" encoding="utf-8"?>
        
        self.data=     '''<?xml version="1.0" encoding="utf-8"?>
                <LowPricePolicyListRequest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:ctrip:api:flight:trade:message:lowPricePolicy:v1">
                <MessageHead>
                <UserInfo xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">
                <UserName>'''+self.name+'''</UserName>
                <Password>'''+self.psw+'''</Password>
                </UserInfo>
                <ClientID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">5</ClientID>
                <RequestGUID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">'''+str(self.id)+'''</RequestGUID>
                </MessageHead>
                <MessageBody>
                <SearchCondition>
                <Airline>KN</Airline>
                <EffectDate>'''+str(self.yearDate)+'''T00:00:00</EffectDate>
                <DepartPort>'''+str(self.DepartPort)+'''</DepartPort>
                <ArrivePort>'''+str(self.ArrivePort)+'''</ArrivePort>
                <GoSubClass />
                <TradePolicyType>SPECIALPOLICY</TradePolicyType>
                <ShareProductTypeList>
                <item>TravelPackage</item>
                </ShareProductTypeList>
                <IsRealTimeData>False</IsRealTimeData>
                </SearchCondition>
                </MessageBody>
                </LowPricePolicyListRequest>'''

        self.post_headers = {'Host':'exchdata.ctrip.com','Content-type':'application/json',
                             }  #'Content-length':"%d" % len(data2)
    def get_data(self):
        proxies = {"http": "http://58.220.2.132:80",
                   "https": "http://58.220.2.133:80",
                   "https": "http://58.220.2.134:80",
                   "https": "http://58.220.2.135:80",
                   "https": "http://58.220.2.136:80",
                   "https": "http://58.220.2.137:80",
                   "https": "http://58.220.2.138:80",
                   "https": "http://58.220.2.139:80",
                   "https": "http://58.220.2.140:80",
                   "https": "http://58.220.2.141:80"
                   }


        try:
            r = requests.post(url=self.url,data=self.data,headers=self.post_headers)
            xml_str = (r.text).lower()
            #print(xml_str)
            ret =r'<policyid>(\d+)</policyid>.*?<costprice>(.*?)</costprice>.*?<flight>(.*?)</flight>'
            ret = re.compile(ret)
            info_list =re.findall(ret,xml_str)
            #print('携程找到航班:%s'%info_list)

            #log_set(name='class_xiecheng', msg ='[xiecheng]携程找到航班:%s,%s'%(info_list,self.yearDate))
            return info_list
        except:
            print('can not online')

def compare(self,feiba_info,day,deptCd,arrCd):
        """
	    feiba_inf    {'KN5851': ('A', '578.0')}
		xc[('139.94', 'KN2908'), ('397.09', 'KN2906')
		"""
        push_info=''
        info_list = self.get_data()
        #print('xc_info',info_list)
        #print('feba_info',feiba_info)
        if info_list:
           for xc in info_list:
               fligh_name_feiba = (list(feiba_info)[0].encode('utf-8')).lower()
               xc_flight_no = (xc[2]).encode('utf-8').lower()

               #print(xc_flight_no,fligh_name_feiba)
               if xc_flight_no == fligh_name_feiba:    # flight
                   # print('有对应的航班:%s'%(xc[1]).upper())
                   #log_set(name='class_xiecheng', msg ='[xiecheng]有对应的航班:%s'%(xc[1]).upper())
                   feiba_price = feiba_info[fligh_name_feiba.upper()][1].encode('utf-8')
                   inVent =feiba_info[fligh_name_feiba.upper()][0].encode('utf-8')
                   #print(inVent)
                   xc_id = get2_id_from_info(self.yearDate, self.DepartPort,self.ArrivePort,fligh_name_feiba[2:])
                   if inVent in (1,'1'):
                       del_work(xc_id)
                   #if 778.0 - float(feiba_price) >6:
                   #print('----------',float(xc[1]),float(feiba_price))
                   if float(xc[1]) - float(feiba_price) >6:      #推送条件
                       if self.tag in (1,'1'):  # yi tou
                           old_xc_price = get2_pri_from_info(self.yearDate, self.DepartPort,self.ArrivePort,fligh_name_feiba[2:])
                           if not (str(xc[0])).encode('utf-8') == xc_id:   #bie ren gai
                               #print('old_price'+str(old_xc_price)+'NEW PRICE'+str(float(xc[1])))
                               xx =float(xc[1])-float(old_xc_price)
                               if (not (str(xx) == '0.1')):  # bu shi wo
                                   price = str(float(xc[1])-0.1)
                                   #print(xc_id,self.yearDate,price,self.DepartPort,self.ArrivePort,fligh_name_feiba[2:])
                                   log_set(name='fix',msg='%s,me%s,will fix price,last time I push:%s,now xcprice:%s,i will push:%s,feibaflight:%s'%(xc[0],xc_id,old_xc_price,xc[1],price,feiba_price))
                                   inVent= feiba_info[fligh_name_feiba.upper()][0].encode('utf-8')

                                   fix_work(xc_id,self.yearDate,price,self.DepartPort,self.ArrivePort,fligh_name_feiba[2:],inVent)
                               else:
                                   #print('yanshi ,bugaijia')
                                   log_set(name='lunxun_xiecheng', msg='yanshi bu gai jia,old_price'+ str(old_xc_price)+'NEW PRICE'+str(float(xc[1])))
                           else:
                               #print('woziji bu gai jia')
                               log_set(name='lunxun_xiecheng', msg='woziji bu gai jia,old_price'+ str(old_xc_price)+'NEW PRICE'+str(float(xc[1])))
                               pass #shi wo
                   else:
                       #print('need delete zhe push order')
                       log_set(name='lunxun_xiecheng', msg = '[delete]need delete zhe push order,%s,%s,xiecheng:%s,feiba:%s'%(xc[2],self.yearDate,xc[1],feiba_price))
                       #print('delete the pushed order')
                       log_set(name='fix',msg='delete the pushed order:%s,%s,%s,%s,%s'%(self.yearDate, self.DepartPort,self.ArrivePort,fligh_name_feiba[2:],xc_id))
                       #print('idddddd',xc_id)
                       del_work(xc_id)

               else:
                    print('��程没有相应的航班')
        else:
            #print('can not get data form xiecheng')
            log_set(name='lunxun_xiecheng',msg='can not ge date from xiecheng')
        return push_info


def home(day, deptCd, arrCd,feiba_info,tag):
    do_work = DoXC (yearDate=day ,DepartPort=deptCd,ArrivePort=arrCd ,tag=tag)
    log_set(name='class_xiecheng', msg ='###################################.%s,%s,%s,%s,%s'%(day, deptCd, arrCd,feiba_info,tag))
    info = do_work.compare(feiba_info,day, deptCd,arrCd)
    ## print(info)
    #return info

if __name__ == '__main__':
        now =datetime.now()
        feiba_info ={'KN5830': ('3', '140.0')}
        DepartPort="SYX"
        ArrivePort="NAY"
        day ='2015-11-10'
        tag =1
        #print(day, DepartPort, ArrivePort,feiba_info,tag)
        home(day, DepartPort, ArrivePort,feiba_info,tag)
