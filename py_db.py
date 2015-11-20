
#coding=utf-8
import MySQLdb
import time
from my_log import log_set


def do_sql(sql):

    conn= MySQLdb.connect(
            host='127.0.0.1',
            port = 3306,
            user='root',
            passwd='root',
            db = 'xiecheng',
            )
    cur = conn.cursor()

    ret = cur.execute(sql)
    #sql = " select * from fly where fly_no =%s"%fly_no

    #创建数据表
    #cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
    #插入一条数据
    #cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
    #修改查询条件的数据
    #cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
    if 'select' in sql:
        return cur.fetchmany(ret)
    cur.close()
    conn.commit()
    conn.close()
    return ret

def query_xcinfo():
    sql = " select * from fly_xc "
    ret = do_sql(sql)

    return ret


def del_db_xcinfo(id):
    sql = " DELETE FROM fly_xc where xc_id ='%s'"%id
    print(sql)
    try:
        ret = do_sql(sql)
        log_set(name='sql',msg='del_DB,id=%s'%id)
        return ret
    except Exception as e:
        log_set(name='sql', msg='%s,deldb_1 is fail:%s'%(str(e.message),sql))

def update_xcfly(YearMonthDate1,DepartPort, ArrivePort,Flight_Price,Flight_No,inVent,xc_id):
    all_uni = str(YearMonthDate1)+str(DepartPort)+str(ArrivePort)+str(Flight_No)
    sql = """update fly_xc set xc_id ='{}',Flight_Price ='{}',inVent ='{}'
          WHERE all_uni ='{}'""".format(xc_id,Flight_Price,inVent,all_uni)
    try:
        print(sql)
        ret = do_sql(sql)
        log_set(name='sql', msg='update_1 is %s'%(sql))
        return ret
    except Exception as e:
        print('b')
        log_set(name='sql', msg='%s,update_1 is fail:%s'%(str(e.message),sql))

def save_xc_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No,Flight_Price,inVent,xc_id):
    all_uni = str(YearMonthDate1)+str(DepartPort)+str(ArrivePort)+str(Flight_No)
    sql = "insert into fly_xc(YearMonthDate1,DepartPort,ArrivePort,Flight_No,Flight_Price,inVent,xc_id,all_uni) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(YearMonthDate1,DepartPort,ArrivePort,Flight_No,Flight_Price,inVent,xc_id,all_uni)
    print(sql)

    try:
        ret = do_sql(sql)
        log_set(name='sql', msg='[save1_fly_xc],%s'% all_uni)
        return ret
    except Exception as e:
        log_set(name='sql', msg='save1 %s,%s,%s,%s,%s,%s,%s'(str(e),str(YearMonthDate1),str(DepartPort),str(ArrivePort),str(Flight_No),str(Flight_Price),str(inVent)))
        update_xcfly(YearMonthDate1,DepartPort,ArrivePort,Flight_Price,Flight_No,inVent,xc_id)


def update2_xcfly(YearMonthDate1,DepartPort,ArrivePort, Flight_No,price,xc_id,iVent):
    all_uni = str(YearMonthDate1)+str(DepartPort)+str(ArrivePort)+str(Flight_No)
    try:
        sql = " update fly_xc2 set xc_id ='%s',price ='%s',inVent ='%s' WHERE  all_uni='%s'"%(xc_id, price, iVent,all_uni)
        print(sql)
        ret = do_sql(sql)
        log_set(name='sql', msg='[update2_save] is ok,%s,%s,%s,%s,%s,%s,%s+%s'%(str(YearMonthDate1),str(DepartPort),str(ArrivePort),str(Flight_No),str(price),str(xc_id),iVent,sql))
        return ret
    except Exception as e:

        log_set(name='sql', msg= '%s,update2 is fail,%s'%(str(e.message),str(sql)))


def save2_xc_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No,inVent,xc_id,price):
    all_uni = str(YearMonthDate1)+str(DepartPort)+str(ArrivePort)+str(Flight_No)
    sql = "insert into fly_xc2(YearMonthDate1,DepartPort,ArrivePort,Flight_No,inVent,xc_id,all_uni,price) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(YearMonthDate1,DepartPort,ArrivePort,Flight_No,inVent,xc_id,all_uni,price)
    print(sql)
    try:
        ret = do_sql(sql)
        log_set(name='sql',msg='[save2]%s'%all_uni)
        return ret
    except Exception as e:
        time.sleep(2)
        log_set(name='sql', msg='%s,save2_fial_to update:%s'%(str(e.message),sql))
        update2_xcfly(YearMonthDate1,DepartPort,ArrivePort, Flight_No,price,xc_id,inVent)
def get2_id_from_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No):
    sql = " select xc_id from fly_xc2 WHERE YearMonthDate1='%s' AND DepartPort='%s' AND ArrivePort='%s' AND Flight_No='%s'"%(YearMonthDate1, DepartPort,ArrivePort, Flight_No)
    print(sql)
    ret = do_sql(sql)
    try:
        return ret[0][0]
    except:
        return None

def get2_pri_from_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No):
    sql = " select price from fly_xc2 WHERE YearMonthDate1='%s' AND DepartPort='%s' AND ArrivePort='%s' AND Flight_No='%s'"%(YearMonthDate1, DepartPort,ArrivePort, Flight_No)
    print(sql)
    try:
        ret = do_sql(sql)
        return ret[0][0]
    except:
        return 0


def del2_xcinfo(id):
    sql = " DELETE FROM fly_xc2 where xc_id ='%s'"%id
    print(sql)
    try:
        ret = do_sql(sql)
        log_set(name='sql',msg='del_DB2,id=%s'%id)
        return ret
    except Exception as e:
        log_set(name='sql', msg='%s,deldb_2 is fail:%s'%(str(e.message),sql))
def get_id_from_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No):
    sql = " select xc_id from fly_xc WHERE YearMonthDate1='%s' AND DepartPort='%s' AND ArrivePort='%s' AND Flight_No='%s'"%(YearMonthDate1, DepartPort,ArrivePort, Flight_No)
    print(sql)
    ret = do_sql(sql)
    try:
        return ret[0][0]
    except:
        return None


if __name__=='__main__':
    YearMonthDate1='1'
    DepartPort='2'
    ArrivePort='3'
    Flight_No='4'
    inVent='5'
    xc_id='6'
    price='7'
    # save2_xc_info(YearMonthDate1, DepartPort,ArrivePort, Flight_No,inVent,xc_id,price)
    #a = get2_id_from_info('1015-11-44','Nay','JJJ','7899')
    #print(a,type(a))
    sql ='delete from fly_xc'
    do_sql(sql)
    sql ='delete from fly_xc2'
    do_sql(sql)
