import requests
import time


def is_ok(proxies):
    url = 'http://www.ip138.com/'
    r = requests.get(url, proxies=proxies)
    if r.status_code == 200:
        return proxies


def get_ip(num):
    time.sleep(1)
    url = 'http://vxer.daili666api.com/ip/?tid=559563727758531&num=%s\
        &filter=on' % num
    r = requests.get(url)
    i = (r.content)
    print('get ip',i)
    IP_list = list()
    b = i.split('\r\n')
    for g in b:
        g = "{'http':'http://"+g+"'}"
        # print(g)
        d = eval(g)
        # d = is_ok(d)
        IP_list.append(d)
        # if not len(IP_list):
        # get_ip()
    return IP_list
if __name__ == '__main__':
    print(get_ip(1))
