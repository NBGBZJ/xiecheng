
import multiprocessing
import thread
def pr(a):
    print(str(a) + 'a')
b='aaaa'
for i in range(0, 2):
    print(i)
    thread.start_new_thread( pr, ("Thread-1", i, ) )
