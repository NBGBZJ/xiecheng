
# -*- coding:utf-8 -*-
import requests
import hashlib
import uuid
import sys
import re
from py_db import update2_xcfly

reload(sys)
sys.setdefaultencoding('utf-8')
from my_log import log_set


class Fix_XieChenData:
    def __init__(self,xc_id,date,price,DepartPort,ArrivePort,Flight_No):
        self.name = "政策管理"
        self.psw = hashlib.md5('政策管理#a1234567').hexdigest().upper()
        self.uuid = str(uuid.uuid1())
        self.url = 'http://exchdata.ctrip.com/Flight-Proxy-TradeQuickAPI/api/xml/SpecialPolicyChangePrice '
        self.xc_id = str(xc_id)

        self.date = date
        self.price = str(price)
        self.DepartPort = str(DepartPort)
        self.ArrivePort = str(ArrivePort)
        self.Flight_No = str(Flight_No)

        self.data='''<?xml version="1.0"?>
<SpecialPolicyChangePriceRequest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:ctrip:api:flight:trade:message:specialPolicy:v1">
  <MessageHead>
    <UserInfo xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">
      <UserName>'''+self.name+'''</UserName>
      <Password>'''+self.psw+'''</Password>
    </UserInfo>
    <ClientID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">4</ClientID>
    <RequestGUID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">%s</RequestGUID>
  </MessageHead>
  <MessageBody>
    <PolicyList>
      <Policy>
        <PolicyID>%s</PolicyID>
        <IsValid>T</IsValid>
        <PriceUnit>
          <SetPrice>%s</SetPrice>
        </PriceUnit>
      </Policy>
    </PolicyList>
  </MessageBody>
</SpecialPolicyChangePriceRequest>'''% (self.uuid,self.xc_id,self.price)

        self.post_headers = {'Host':'exchdata.ctrip.com','Content-type':'application/json',
                             }  #'Content-length':"%d" % len(data2)

    def get_data(self):

        r = requests.post(url=self.url,data=self.data,headers=self.post_headers)
        xml =str(r.text)
        #print(xml)
        re_e = r'FailedCount>(\d+)'
        res = re.compile(re_e)
        fail_info =re.findall(res, xml)

        try:
            if int(fail_info[0]):

                log_set(name='fix', msg='fix is fail ,do it youself,id =%s' % self.xc_id)
                return False
            else:
                print('fixied')
                log_set(name='fix', msg=' fix is ok!,id =%s,%s,%s,%s,%s,%s'% (self.date,self.DepartPort,self.ArrivePort,self.Flight_No,self.price,self.xc_id))
                print(self.date,self.DepartPort,self.ArrivePort,self.Flight_No,self.price,self.xc_id)
                update2_xcfly(self.date,self.DepartPort,self.ArrivePort,self.Flight_No,self.price,self.xc_id)
                print('fix is successs,%s' % self.id)
                return True

        except:
              #log_set(name='del_info', msg='[Del_XC_Fail2]deal error, please check!,id =%s'% self.id)
              #return False
              pass
def fix_work(xc_id,date,price,DepartPort,ArrivePort,Flight_No):

    do_work = Fix_XieChenData(xc_id,date,price,DepartPort,ArrivePort,Flight_No)
    return do_work.get_data()

if __name__ == '__main__':
    xc_id = '134270588004'
    data='2015-11-09'
    price='2000'
    DepartPort = 'DSN'
    ArrivePort = 'CSX'
    Flight_No = '2809'

    fix_work(xc_id,data,price,DepartPort,ArrivePort,Flight_No)
