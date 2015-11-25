from py_db import query_xcinfo
from class_xiecheng_lunxun import home
from my_log import log_set
import time
import copy
from multiprocessing import Pool

def fenduan(a):
    l = list()
    t=len(a)/5+1
    for i in range(t):
        b = a[i*5:5*(i+1)]
        l.append(b)
    return(l)


def home2(xc_list):
   
    for i in xc_list:
        fb_info = dict()
        flight_name=('KN'+i[3])   #kn5858
        fb_info[flight_name] =(i[5], i[4])
        print(fb_info)
        day=i[0]
        deptCd=i[1]
        arrCd=i[2]
        tag=1
        print(day, deptCd, arrCd,fb_info,tag)
        # time.sleep(0.5)
        home(day, deptCd, arrCd, fb_info,tag)
        

def lunxun():
    while(1): 
        xc_list = query_xcinfo()
        print('lunxun'+str(xc_list))
        t = len(xc_list)
        print(t)

        if t :
            xc_list2 = copy.deepcopy(xc_list)
            print(len(xc_list2))
            l = fenduan(xc_list2)
            pool = Pool(processes=len(l))
            for i in range(len(l)):
                print(len(l))
                print(l[i])
                #a=input()
                result = pool.apply_async(home2,(l[i],))
            pool.close()
            pool.join()
        else:
            time.sleep(5)
            lunxun()
            
if __name__ == '__main__':
    lunxun()
