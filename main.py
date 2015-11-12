from tongbu import tongbu
import multiprocessing
from fb_xc import lunxun
from my_log import log_set

def work():
    # g = multiprocessing.Process(target = lunxun)
    # g.start()
    with open('hx.txt', 'r') as f:
        cont = f.readlines()


    for i in range(0,9):
        print(i)
        hangxian = cont[i].replace('\r\n', '')
        hangxian = [x for x in hangxian.split("'") if x.isalpha()]
        #print(type(hangxian))

        p = multiprocessing.Process(target = tongbu, args= (hangxian[0], hangxian[1]))
        p.start()
        log_set(name='hangxian',msg= (str(i)+str(hangxian[0])+str(hangxian[1])))

if __name__ == "__main__":
    work()
