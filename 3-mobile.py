# -*- coding:utf-8 -*-
import requests
import random
import urllib2
import cookielib
import urllib
import json
import pickle


session = requests.Session()


url = 'https://58.83.164.131/cuaMo-webapp/flight?org=PEK&dst=SHA&goFlightDate=2015-11-02&fltclass=CY'



user_agent = ("Mozilla/5.0 (Linux; U; Mobile; Android 4.4.2;HONOR H30-L01M Build/FRF91")



post_headers = {'Accept': '*/*',
				'Accept-Encoding': 'gzip, deflate',
				'Cookie':'AlteonP=3db2f5a10a6e50ec6f7a21351f90; JSESSIONID=gjGyWs6TclTRQrb8svZnrQJL5z189pzSpyYnvSjDcdZd6D1ZSBDZ!-1088095172!223106076',
				'appverify': 'md5=25aea2e014207f8d39251f9b7dbe305c;ts=1445757618307'
                }

response = session.post(url,headers=post_headers, verify=False)

Cdata = response.json()
print Cdata

