import time
from main import work
from my_log import log_set
i = 0
while 1:
    print(i)
    work()
    time.sleep(60*6)

    i+=1
    #log_set(name='runtime', msg='the times:%s'%i)

