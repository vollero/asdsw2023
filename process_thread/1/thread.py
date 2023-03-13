from multiprocessing import Process
from threading import Thread
from time import *
from random import *

shared_x = randint(10,99)

def sleeping(name):
    global shared_x
    s = randint(1,20)
    sleep(s)
    shared_x = shared_x + 1

    t = gmtime()
    s = randint(1,20)
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds'
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up, seeing shared_x being ' + str(shared_x)
    print(txt)


def sleeper(name):
    sleeplist = list()

    global shared_x
    shared_x = randint(10,99)

    for i in range(3):
        subsleeper = Thread(target=sleeping, args=(name + ' ' + str(i),))
        sleeplist.append(subsleeper)

    txt = name + ' sees shared_x being ' + str(shared_x)
    print(txt)

    for s in sleeplist: s.start()
    for s in sleeplist: s.join()

    txt = name + ' sees shared_x being ' + str(shared_x)
    print(txt)


   
if __name__ == '__main__':
    p = Process(target=sleeper, args=('eve', ))
    q = Process(target=sleeper, args=('bob', ))

    p.start(); q.start()
    p.join(); q.join()
