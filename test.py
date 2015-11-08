#coding=utf-8
#对话框
import sys
from PyQt4 import QtGui, QtCore
import requests
import xml
import json
import xml.dom.minidom
import hashlib
import uuid
import sys
import urllib2
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "hello" )
        self.resize( 500, 500 )

        self.button1 = QtGui.QPushButton( u"点击") #初始化按钮
        self.button2 = QtGui.QPushButton( u"点击" )
        self.textArea = QtGui.QTextBrowser()##初始化显示文本框，不是输入
        self.textArea.setPlainText(u'数据开始显示：')

        sbox = QtGui.QHBoxLayout()#水平空间设置
        #sbox.addStretch(1) 伸缩空间
        sbox.addWidget(self.button1)
        sbox.addStretch(1)
        sbox.addWidget(self.button2)

        hbox = QtGui.QVBoxLayout()
        hbox.addLayout(sbox)#关键 把水平空间加入到垂直空间
        hbox.addWidget(self.textArea)

        self.setLayout(hbox)

        self.connect(self.button1,QtCore.SIGNAL('clicked()'),self.updateUi)

    def updateUi(self):
        self.textArea.append(rrr.decode('ascii', 'ignore').encode('utf-8'))###将内容输入到textBrowser


#####携程post类

class Get_XieChenData:
    def __init__(self,url,data):
        self.url = url
        self.data = data
        self.post_headers = {'Host':'exchdata.ctrip.com','Content-type':'application/json',
                             'Content-length':"%d" % len(data2)}

    def get_data(self):
        r = requests.post(url=self.url,data=self.data,headers=self.post_headers) 
        s = r.content
        return s.decode('ascii', 'ignore').encode('utf-8')    

if __name__ == '__main__':      
    
    name = "外部测试1"
    psw = hashlib.md5('外部测试1#Ctrip@1').hexdigest().upper()
    id = uuid.uuid1()
    #特殊政策url
    url = 'http://exchdata.ctrip.com/Flight-Proxy-TradeQuickAPI/api/xml/LowPricePolicyList'
    #查询所有

    data2=     '''<?xml version="1.0" encoding="utf-8"?>
                <LowPricePolicyListRequest xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:ctrip:api:flight:trade:message:lowPricePolicy:v1">
                <MessageHead>
                <UserInfo xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">
                <UserName>'''+name+'''</UserName>
                <Password>'''+psw+'''</Password>
                </UserInfo>
                <ClientID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">5</ClientID>
                <RequestGUID xmlns="urn:ctrip:api:flight:trade:common:baseType:v1">'''+str(id)+'''</RequestGUID>
                </MessageHead>
                <MessageBody>
                <SearchCondition>
                <AirLine />
                <EffectDate>2015-11-26T00:00:00</EffectDate>
                <DepartPort>CAN</DepartPort>
                <ArrivePort>HGH</ArrivePort>
                <GoSubClass />
                <TradePolicyType>SPECIALPOLICY</TradePolicyType>
                <ShareProductTypeList>
                <item>PriorityPackage</item>
                <item>Limited</item>
                <item>ApplySpecial</item>
                <item>TravelPackage</item>
                <item>AirLineMarketing</item>
                <item>NA</item>
                </ShareProductTypeList>
                <IsRealTimeData>False</IsRealTimeData>
                </SearchCondition>
                </MessageBody>
                </LowPricePolicyListRequest>'''

    do_work1=Get_XieChenData(url,data2)
    oo = do_work1.get_data()
    soup = BeautifulSoup(''.join(oo),"lxml") ##解析xml

    Flight = soup.find_all('flight') #航班号
    CostPrice = soup.find_all('costprice') ##价格
    DepartDate = soup.find_all('departdate') ## 出发日期

    get_flight = []
    for aa in Flight:
        aaa= aa.contents
        get_flight.append(aaa)

    get_price = []
    for bb in CostPrice:
        bbb= bb.contents
        get_price.append(bbb)

    get_date = []   
    for cc in DepartDate:
        ccc = cc.contents
        get_date.append(ccc)


    rr = []
    for i in xrange(len(get_date)):
        rr.append( ("Flight NO %s,  DepartDate  %s,  PRICE  %s " %(get_flight[i][0],get_date[i][0],get_price[i][0])))
      
    

    rrr = str(rr)
    app = QtGui.QApplication( sys.argv )
    win = Window()
    win.show()
    app.exec_()