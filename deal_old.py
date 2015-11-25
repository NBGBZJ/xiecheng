from py_db import sel_old
from class_xiecheng_delete import del_work
from py_db import get2_id_from_info
def del_old(YearMonthDate, deptCd, arrCd, all_hyl):
    day = YearMonthDate
    depart = deptCd
    arr = arrCd
    fly_no_list = sel_old(day,depart,arr)
    print(fly_no_list)
    new_flyno = list()
    if len(all_hyl)>0:
        for i in all_hyl:
            i = list(i)
            new_flyno.append(i[0][2:].decode('utf-8'))
        print(new_flyno)
        for j in  fly_no_list:
            if j[0] not in new_flyno:
                xc_id = get2_id_from_info(YearMonthDate,deptCd,arrCd,j[0])
                del_work(xc_id)
        



if __name__=='__main__':
    YearMonthDate = '2015-11-28'
    deptCd = 'NAY'
    arrCd = 'SZX'
    all_hyl = [{u'KN5857': (u'3', u'798.0')}, {u'KN5911': (u'2', u'898.0')}]
    
    del_old(YearMonthDate, deptCd, arrCd,all_hyl)
