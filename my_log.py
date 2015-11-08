

from datetime import datetime, timedelta
import os


PWD = 'a1234567'


FILE_path = os.getcwd() +'/log_jiexheng/'

def log_set(msg, name ='main'):
    now_time = datetime.now()
    yes_date = now_time + timedelta(days=-1)
    str_now = str(now_time).split('.')[0]
    str_yes = str(yes_date).split('.')[0]
    FILE_yes = FILE_path +'%s%s'%(name, str_yes)
    FILE_main = FILE_path +'%s%s'%(name, str_now)
    #print(FILE_yes[:-9],FILE_main[:-9])
    try:
        os.system('mkdir -p %s ;touch %s' % (FILE_path, FILE_main[:-9]))
        #os.system('mkdir -p %s ;rm %s ;touch %s' % (FILE_path, FILE_yes[:-9],FILE_main[:-9]))
    except:
        pass
    f = open('%s' % FILE_main[:-9], 'a+')
    f.write('[' + str(datetime.now()).split('.')[0] + ']' + msg + '\n')
    f.close()

#log_set(name ='a',msg ='hia')
# log_set(msg ='hia2')
log_set(name='fix', msg=' fix is ok!,id =%s')
