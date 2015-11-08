# -*- coding:utf-8 -*-
import requests
import hashlib
import uuid
import sys
import re
from py_db import del_db_xcinfo,del2_xcinfo

reload(sys)
sys.setdefaultencoding('utf-8')
from my_log import log_set


class Delete_XieChenData:
    def __init__(self,id):
        self.name = "政策管理"
        self.psw = hashlib.md5('政策管理#a1234567').hexdigest().upper()
        self.uuid = uuid.uuid1()
        self.id = id
        self.url = 'http://exchdata.ctrip.com/Flight-Proxy-TradeQuickAPI/api/xml/SpecialPolicyDelete'
        
        self.data='''<?xml version="1.0"?>
<SpecialPolicyDeleteRequest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:ctrip:api:flight:trade:message:specialPolicy:v1">
  <MessageHead>
    <UserInfo xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">
      <UserName>'''+self.name+'''</UserName>
      <Password>'''+self.psw+'''</Password>
    </UserInfo>
    <ClientID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">5</ClientID>
    <RequestGUID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">'''+str(self.uuid)+'''</RequestGUID>
  </MessageHead>
  <MessageBody>
    <DeleteType>ByCode</DeleteType>
    <PolicyIDList />'''+str(self.id)+'''<PolicyIDList />
    <PolicyCodeList>
      <Code>AAA-1</Code>
    </PolicyCodeList>
    <ExternalIDList />
    <PolicySource>QuickAPI</PolicySource>
  <IsFuzzyMatch>F</IsFuzzyMatch>
  </MessageBody>
</SpecialPolicyDeleteRequest>''' 

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
                log_set(name='del_info', msg='[Del_XC_Fail]del is fail ,do it youself,id =%s' % self.id)
                return False
            else:
                log_set(name='del_info', msg='[Del_XC_Ok] del_XC is ok!,id =%s'% self.id)
                del2_xcinfo(self.id)
                print('xiaohui is successs,%s'%self.id)
                return True

        except:
              log_set(name='del_info', msg='[Del_XC_Fail2]deal error, please internater!,id =%s'% self.id)
              #return False


def del_work(xc_id):
    print('deling')
    del_db_xcinfo(xc_id)
    log_set(name='del_info', msg='will to de,id =%s'%xc_id)

    do_work = Delete_XieChenData(xc_id)
    del2_xcinfo(xc_id)
    return do_work.get_data()

if __name__ == '__main__':
    xc_id = '134285814868'
    del_work(xc_id)
