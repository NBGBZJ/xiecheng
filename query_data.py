#-*-coding:utf-8-*-
from collections import OrderedDict
import hashlib
import time
import requests

from requests.compat import (
    unquote,
    urlencode,
)

"""
zhengshi:goods.api.7lk.com
 ceshi:goodsapi.test.7lk.cn
 开发kgoodsapi.7lk.cn
"""

URL = 'http://goodsapi.7lk.cn/base/goods-indexes'
#URL = 'http://goods.api.7lk.com/base/goods-indexes'
private_key = 'goodsapi@7lk.com'


def build_url(url, qs=''):

        if qs:
            url += '?' + qs
        print(url)
        return url

def query_hph( method='get', **argvs):

        data = OrderedDict(sorted(argvs.items(), key=lambda t: t[0]))
        time_s = int(time.time())
        data_str = unquote(urlencode(data))
        hash_str = 'private_key={0}&ts={1}&{2}'.format(private_key,
                                                       time_s,
                                                       data_str)

        sign = hashlib.md5(hash_str.encode('utf-8')).hexdigest()
        data.update({'sign': sign, 'ts': str(time_s)})

        par_str = unquote(urlencode(data))
        url = build_url(url=URL, qs=par_str)
        try:
            response = requests.get(url)
            response_dict = response.json()

        except requests.RequestException as e:
            return False
        response_code = response_dict.get('code')
        if response_code == 0:
            return response_dict['data']
        else:
            print('no info')
            return False


def change_time(a):
    try:
        timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp
    except:
        print('change time is fail')
        return False




def get_phq_good_list(start,end,page=5):
    """
    :param start:  '2015-01-01 11:11:11'
    :param end: '2015-11-11 11:11:11'
    :param page: '1'
    :return:{u'msg': u'success', u'code': 0, 'date':{,gquery_data.pyoods_list[{},{}]}
    """
    start=change_time(start)
    end=change_time(end)
    data = query_hph(start=start, end=end, page=page)
    total = data['total']
    goods_list = data['goods_list']
    res_list = goods_list
    for i in range(2, total):
        data = query_hph(start=start,end=end,page=page)
        goods_list = data['goods_list']
        res_list += goods_list
    return res_list

def cmp(goods_list):
    print(len(goods_list))
    for one_goods in goods_list:

        url = 'http://assist.7lk.cn:8000/test/goods/?goods_id=%s' % one_goods['id']
        print(url)
        # try:
        res = (requests.get(url).json())[0]
        print(one_goods['buy_price'],res['buy_price'])
        fag = 1
        res['id'] = res['goods_id']
        one_goods['buy_price'] =float('%0.2f'%(one_goods['buy_price']()))
        res['buy_price'] = float('%0.2f'%(res['buy_price']))
        # print(one_goods['buy_price'],res['buy_price'])
        # res['buy_price'] =str(float('%0.2f'%((float(res['buy_price'])/10))))

        for key in one_goods:
            if res.get(key):
                if res.get(key) == one_goods[key]:
                    print('same:'+str(key))
                else:
                    print('diff',res['id'],key ,one_goods[key], res.get(key))
                    fag = 0
        if fag:
            print('is OK!')

        else:
            print('fail update')
            return False
        # except:
            # print("can't request the right data")

if __name__ == '__main__':
    php_date =get_phq_good_list('2015-10-03 11:11:11','2015-11-11 11:11:11')
    cmp(php_date)