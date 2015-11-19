import time
from main import work
import os
from my_log import log_set
from give_ip import get_all_ip
i = 0
while 1:
    print(i)
    os.system('rm /home/fuhan/python2.7-env/xiecheng/ip_list0.txt ')
    get_all_ip()
    time.sleep(6)
    work()
    time.sleep(60)

