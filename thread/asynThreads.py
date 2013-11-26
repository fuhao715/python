# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-26
# * Time: 上午10:10
# * To change this template use File | Settings | File Templates.
from threading import Lock, Thread
lock = Lock()
some_var = 0

class IncrementThread(Thread):
    def run(self):
        global some_var
        lock.acquire()
        read_value = some_var
        print "some_var in %s is %d" % (self.name, read_value)
        some_var = read_value + 1
        print "some_var in %s after increment is %d" % (self.name, some_var)
        lock.release()


def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "After 50 modifications, some_var should have become 50"
    print "After 50 modifications, some_var is %d" % (some_var,)

use_increment_thread()