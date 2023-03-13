# See "Distributed Systems" - Van Steen, Tanenbaum - Ed. 4 (p. 117)

from multiprocessing import Process
from time import *
from random import *

def sleeper(name):
    t = gmtime()
    s = randint(1,20)
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds'
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up'
    print(txt)

if __name__ == '__main__':
    p1 = Process(target=sleeper, args=('eve', ))
    p2 = Process(target=sleeper, args=('bob', ))
    p3 = Process(target=sleeper, args=('mike', ))

    p1.start(); p2.start(); p3.start()
    p1.join(); p2.join(); p3.join()
