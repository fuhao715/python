# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-12-4
# * Time: 上午8:49
# * To change this template use File | Settings | File Templates.

'''
解释：

    在原来使用list的位置，改为使用Queue实例（下称队列）。
    这个队列有一个condition，它有自己的lock。如果你使用Queue，你不需要为condition和lock而烦恼。
    生产者调用队列的put方法来插入数据。
    put()在插入数据前有一个获取lock的逻辑。
    同时，put()也会检查队列是否已满。如果已满，它会在内部调用wait()，生产者开始等待。
    消费者使用get方法。
    get()从队列中移出数据前会获取lock。
    get()会检查队列是否为空，如果为空，消费者进入等待状态。
    get()和put()都有适当的notify()。现在就去看Queue的源码吧。
'''

from threading import Thread
import time
import random
from Queue import Queue

queue = Queue(10)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print 'Produced', num
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print 'Consumed', num
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()