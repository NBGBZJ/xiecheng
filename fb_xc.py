from py_db import query_xcinfo
from class_xiecheng_lunxun import home
from my_log import log_set
import time
import copy
import multiprocessing  
"""
YearMonthDate1 ='2015-11-08'
DepartPort = 'DSN'
ArrivePort ='CSX'
Flight_No = 'kn2809'

Flight_Price = '10000'
inVent='4'
xc_id = '133583761429'
print('a')
update_xcfly(YearMonthDate1,DepartPort, ArrivePort, Flight_Price,Flight_No,inVent,xc_id)
#save_xc_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No,Flight_Price,inVent,xc_id)
#save2_xc_info(YearMonthDate1,DepartPort,ArrivePort,Flight_No,inVent,xc_id)
#a=get2_id_from_info('2015-12-09', 'NAY', 'CIF', '2929')
#xc_id = get2_id_from_info(yearDate, self.DepartPort,self.ArrivePort,fligh_name_feiba[2:])

#save_xc_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No,Flight_Price,inVent,xc_id)
#xc_list = query_xcinfo()
#print(type(xc_list))
#print(a)
#del2_xcinfo(a)

#update2_xcfly(YearMonthDate1, DepartPort,ArrivePort, Flight_No,Flight_Price,xc_id)
#xc_list = query_xcinfo()
#print(xc_list)

"""

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
       # a =input()
        if t :
            xc_list2 = copy.deepcopy(xc_list)
            print(len(xc_list2))
            l = fenduan(xc_list2)
            for i in range(len(l)):
                print(len(l))
                print(l[i])
                #a=input()
                p = multiprocessing.Process(target=home2, args =(l[i],))
           #p = multiprocessing.Process(target=home2, args =(t,))
                p.start()
                print('#######################')                        #p = multiprocessing.Process(target=home, args=(i[0], i[1], i[2], fb_info,1))
        else:
            lunxun()
if __name__ == '__main__':
    lunxun()
