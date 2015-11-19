import requests
import time
import json
import  multiprocessing
import random


def yazheng(g):
    IP_list = list()
    g = "{'http':'http://"+g+"'}"
    #print('yanzheng',g)
    d = eval(g)
    if is_ok(d):
        pass
    else:
        c = json.dumps(d, ensure_ascii=False)+ ','
        write_in(c, 0)
        return IP_list


def is_ok(proxies):
    url = 'http://www.flycua.com/member/member-login!login_kn.shtml?redirectUrl=http://www.flycua.com/order/air-order!init.shtml&ltv=1'
    #print(proxies)
    r = requests.get(url, proxies=proxies)
    #print('r.status_code', r.status_code)
    if r.status_code in(200,'200'):
        return 0
    else:
        return 1


def write_in(content,i):
    print('do wirte')
    f = open("ip_list%s.txt"% str(i), "a")
    f.writelines(content)
    f.close()


def read_out(i):
    f = open('ip_list%s.txt'%i)
    content = f.read()
    f.close()
    return content


def get_ip(or_id,num,j):
    try:
        time.sleep(1.3)
        url = 'http://vxer.daili666api.com/ip/?tid=%s&num=%s&delay=5' % (or_id, int(num))
        #print(url)
        r = requests.get(url)
        i = (r.content)
       # print(i)
        IP_list = list()
        if not ('503' in str(i)):
            #print('get ip',or_id,i)
            b = i.split('\r\n')
            #print('b',b)
            for g in b:
                print('g',g)
                IP_listq = multiprocessing.Process(target=yazheng, args=(g, ))
                IP_listq.start()
                # IP_list += IP_listq
            # print('IP_list',IP_list)
            # write_in(json.dumps(IP_list),j)
            print('over 2')
        else:
            print('503')
            get_ip(or_id,num,j)

    except:
        print('online is fail')
        get_ip(or_id, num, j)


def get_all_ip():
    or_list = ['557442251667170', '557119508655222', '559138925024836', '559563727758531']
    for i in range(4):
        p = multiprocessing.Process(target=get_ip, args=(or_list[i],15, i))
        p.start()
        


if __name__ == '__main__':
    #get_all_ip()
    #print(read_out(0))
    or_id = '559448882032955'
    num =10
    i=0
    # get_ip('559138925024836',1,0)
    #get_all_ip()
    ip = read_out(i)
    print(ip, type(ip))
    ip2 = '[' + ip.rstrip(',')  +']'
    print(ip2)
    print(json.loads(ip2, encoding="utf-8"),)

