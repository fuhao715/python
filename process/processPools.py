# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/1
 * Time: 20:30
 * To change this template use File | Settings | File Templates.
'''
# from multiprocessing import Pool
import multiprocessing
import os,time, random

def long_time_task(name):
    print 'Run task %s (%s)....' %(name, os.getpid())
    start = time.time()
    time.sleep(random.random()*30)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
    # return end - start

if __name__ == '__main__':
    print 'Parent process %s .cpu_count: %s ' % (os.getpid(), multiprocessing.cpu_count())
    p = multiprocessing.Pool(processes=4)
    # result = []
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
        # result.append(p.apply_async(long_time_task, args=(i,)))
    print 'Waiting for all subprocess done ....'
    p.close()
    p.join()
    '''
    for res in result:
        print 'result : %s ' %res.get()
    '''
    print 'All subprocesses done.'


