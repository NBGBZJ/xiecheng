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
def lunxun():
    while(1): 
        xc_list = query_xcinfo()
        print('lunxun'+str(xc_list))
        t = len(xc_list)
        # time.sleep(2)
        if t :
            xc_list2 = copy.deepcopy(xc_list)
            for i in xc_list2:
                t -= 1
                time.sleep(1)
                #(('2015-11-09', 'DSN', 'CSX', 'kn2809', '140.0', '3', '133908916025', '2015-11-09DSNCSXkn2809'),)
                #{u'KN5911': (u'A', u'868.0')}
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
                p = multiprocessing.Process(target=home, args =(day, deptCd, arrCd, fb_info,tag))
                p.start()
                                        #p = multiprocessing.Process(target=home, args=(i[0], i[1], i[2], fb_info,1))
        else:
            lunxun()
if __name__ == '__main__':
    lunxun()
