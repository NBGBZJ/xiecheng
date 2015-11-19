# -*- coding:utf-8 -*-
import requests
import xml
import json
import xml.dom.minidom
import hashlib
import uuid
import sys
#import urllib2
from datetime import datetime
from datetime import timedelta
#import BeautifulSoup
import re
#reload(sys)
#sys.setdefaultencoding('utf-8')
from my_log import log_set
from py_db import get2_id_from_info,save2_xc_info,update2_xcfly,save_xc_info

class Post_XieChenData:
    def __init__(self,yearDate,DepartPort,ArrivePort,Flight_No,Flight_Price,inVent,feiba_inVent,feiba_price):
        self.name = "政策管理"
        self.psw = hashlib.md5('政策管理#a1234567').hexdigest().upper()
        self.id = uuid.uuid1()
        self.url = 'http://exchdata.ctrip.com/Flight-Proxy-TradeQuickAPI/api/xml/SpecialPolicyAdd'
        #self.yearDate = yearDate
        self.DepartPort = DepartPort
        self.ArrivePort = ArrivePort
        self.Flight_No = Flight_No
        self.Flight_Price = Flight_Price
        self.inVent = inVent
        self.yearDate = yearDate
        self.now =datetime.now()
        self.feiba_inVent=feiba_inVent
        self.feiba_price=feiba_price

       
        #<?xml version="1.0" encoding="utf-8"?>
        
        self.data='''<?xml version="1.0"?>
        <SpecialPolicyAddRequest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:ctrip:api:flight:trade:message:specialPolicy:v1">
        <MessageHead>
        <UserInfo xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">
      <UserName>'''+self.name+'''</UserName>
      <Password>'''+self.psw+'''</Password>
    </UserInfo>
    <ClientID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">5</ClientID>
    <RequestGUID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">'''+str(self.id)+'''</RequestGUID>
  </MessageHead>
  <MessageBody>
    <PolicyList>
      <Policy>
      <PolicyID>1263621632613621636</PolicyID>
        <SummaryUnit>
          <SupplierPolicyID>878787878787</SupplierPolicyID>
          <Class>Y</Class>
          <AdvanceDay>0</AdvanceDay>
          <MaxAdvanceDay>365</MaxAdvanceDay>
          <RcID xsi:nil="true" />
          <PolicyCode>AAA-1</PolicyCode>
          <PolicySource>All</PolicySource>
          <AirLine>KN</AirLine>
          <FlightWay>S</FlightWay>
          <ApplyChild>F</ApplyChild>
          <DepartPort>'''+str(self.DepartPort)+'''</DepartPort>
          <ArrivePort>'''+str(self.ArrivePort)+'''</ArrivePort>
          <EffectDate>'''+str(self.now)[:10]+'''T00:00:00</EffectDate>
          <ExpiryDate>2015-12-31T00:00:00</ExpiryDate>
          <IsValid>T</IsValid>
          <ProductType>BJ</ProductType>
          <IsSecurity xsi:nil="true" />
          <ApplyFlag xsi:nil="true" />
          <SaleTimeLimit />
          <DateCanSale>T</DateCanSale>
          <PataVerifyPriceOption>0</PataVerifyPriceOption>
          <PassengerAgeLimitRemarks />
          <VouchersType>0</VouchersType>
          <NeedPATA xsi:nil="true" />
          <PataCode />
          <BatchNo xsi:nil="true" />
          <TicketRemark xsi:nil="true" />
        </SummaryUnit>
        <RuleRestrict>
            <Name xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">不得退改签</Name>
          <FeeBasis xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">S</FeeBasis>
          <MinFeeExpense xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">50</MinFeeExpense>
          <RefundRateRemarks xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">100-2-100</RefundRateRemarks>
          <ReroutRateRemarks xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">100-2-100</ReroutRateRemarks>
          <IsEndorse xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">F</IsEndorse>
          <Remarks xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">不得退改签-98989898</Remarks>
        </RuleRestrict>
        <InventoryUnit>
          <InventoryType>FIX</InventoryType>
          <IsBooking>F</IsBooking>
          <FIX>
            <SaledTicketNum>0</SaledTicketNum>
            <TicketInventory>'''+str(self.inVent)+'''</TicketInventory>
          </FIX>
        </InventoryUnit>
        <GoFlightUnit>
          <EffectDate>'''+str(self.yearDate)+'''T00:00:00</EffectDate>
          <ExpiryDate>'''+str(self.yearDate)+'''T00:00:00</ExpiryDate>
          <Days>1234567</Days>
          <SubClass>T</SubClass>
          <IsCanSale>T</IsCanSale>
          <RuleDetail>'''+str(self.Flight_No)+'''</RuleDetail>
          <DepartTimeLimit />
        </GoFlightUnit>
        <PriceUnit>
          <IsCompositionPrice>false</IsCompositionPrice>
          <CompositionPriceRemark />
          <PrintPrice>0</PrintPrice>
          <SalePrice>0</SalePrice>
          <SetPrice>'''+str(self.Flight_Price)+'''</SetPrice>
          <ReturnPrice>0</ReturnPrice>

          <ForceNomal>false</ForceNomal>
        </PriceUnit>
        <PolicyID>1263621632613621636</PolicyID>
      </Policy>
    </PolicyList>
  </MessageBody>
</SpecialPolicyAddRequest>''' 

        self.post_headers = {'Host':'exchdata.ctrip.com','Content-type':'application/json',
                             }  #'Content-length':"%d" % len(data2)

    def push_data(self):
        r = requests.post(url=self.url,data=self.data, headers=self.post_headers)
        xml_str = (r.text).lower()
        #print(xml_str)

        ret =r'<successcount>(\d)</successcount>'
        ret = re.compile(ret)
        info_list = re.findall(ret, xml_str)
        log_set(name='send', msg='[send] check xml!.%s,%s '%(str(info_list[0]), xml_str))
        if len(info_list[0]):
            print('投放成功')

            ret_id =r'<successlist><id>(\d+)'
            ret_id = re.compile(ret_id)
            id_list = re.findall(ret_id, xml_str)
            print(id_list)

            xc_id_new = str(id_list[0])
            old_xc_id = get2_id_from_info(self.yearDate, self.DepartPort,self.ArrivePort,self.Flight_No)
            print(old_xc_id)
            if not old_xc_id :
                save_xc_info(self.yearDate, self.DepartPort,self.ArrivePort,self.Flight_No, self.feiba_price,self.feiba_inVent,xc_id=xc_id_new)
                save2_xc_info(self.yearDate,self.DepartPort,self.ArrivePort, self.Flight_No,self.inVent,xc_id_new,self.Flight_Price)
            else:
                update2_xcfly(self.yearDate,self.DepartPort,self.ArrivePort, self.Flight_No,self.Flight_Price,xc_id_new,self.inVent)

            log_set(name='send', msg='[send] ok!,%s,%s,%s,%s,%s,%s'%(self.Flight_No,xc_id_new,self.inVent,self.DepartPort,self.ArrivePort,self.yearDate))
            return True
        else:
            # print('失败')
            log_set(name='send', msg='[send_fail] %s,%s,%s,%s,%s'%(self.Flight_No,self.inVent,self.DepartPort,self.ArrivePort,self.yearDate))

            return False

def XC_send(YearMonthDate1, DepartPort, ArrivePort, Flight_No,Flight_Price,feiba_inVent,feiba_price):
    ## print (YearMonthDate1, DepartPort,ArrivePort="CIF", Flight_No=2929,Flight_Price=2898,inVent=12)
    # 修正数据A投5，   大于6投4，  5个投3    大于3小于5投2  ，  2投1
    print('xc_send',YearMonthDate1, DepartPort, ArrivePort, Flight_No,Flight_Price,feiba_inVent)

    Flight_No = Flight_No.lower().encode('utf-8')
    ret2 =r'(\d+)'
    ret2 = re.compile(ret2)
    Flight_No =(re.findall(ret2,Flight_No))[0]

    Flight_Price = str(float(Flight_Price)-0.1)
    inVent2 = 100
    if feiba_inVent in (1,2,3,4,5,6,7,8,9,'1','2','3','4','5','6','7','8','9'):
        if feiba_inVent in (1,'1'):
            inVent =100
        if feiba_inVent in (2,'2'):
            inVent =1
        if feiba_inVent in (3,4,'3','4'):
            inVent = 2
        if feiba_inVent in ('5',5):
            inVent = 3
        if feiba_inVent in ('6','7','8','9',6,7,8,9):
           inVent = 4
    else:
        inVent = 5
    print(inVent)
    if inVent != 100:
        dowork = Post_XieChenData(yearDate=YearMonthDate1,DepartPort=DepartPort,ArrivePort=ArrivePort,
                                  Flight_No=Flight_No ,Flight_Price=Flight_Price,inVent=inVent,feiba_inVent=feiba_inVent,feiba_price=feiba_price)
        # log_set(name='send', msg='[send_fail,yupiao bugou] %s,%s,%s,%s,%s,%s'%(YearMonthDate1, DepartPort, ArrivePort, Flight_No,Flight_Price,feiba_inVent))

        return dowork.push_data()


if __name__ == '__main__':
    now =datetime.now()
    a = timedelta(days=50)
    #YearMonthDate1 = str(now+a)[:10]
    #('2015-11-30', 'NAY', 'SZX', 'kn5857', '577.9', 5)
    YearMonthDate = '2015-11-18'
    DepartPort="DSN"
    ArrivePort="CSX"
    Flight_No='2009'
    Flight_Price='11111'
    feiba_price ='4444'
    inVent= 2
    xc_id='8884g'
    XC_send(YearMonthDate, DepartPort, ArrivePort, Flight_No,Flight_Price,inVent,feiba_price )
    # save2_xc_info(YearMonthDate, DepartPort,ArrivePort, Flight_No,inVent,xc_id,Flight_Price)
    # a = get2_id_from_info(YearMonthDate, DepartPort,ArrivePort, Flight_No)
    # print(a)

    #dowork = Post_XieChenData(YearMonthDate, DepartPort,ArrivePort, Flight_No,Flight_Price,inVent)
    #dowork.push_data()
    #update_xcfly(YearMonthDate, DepartPort="NAY",ArrivePort="CIF", Flight_No='5857',inVent=12,xc_id='888888')


