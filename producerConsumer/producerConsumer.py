# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-12-4
# * Time: 上午8:38
# * To change this template use File | Settings | File Templates.

'''

    在加入数据前，生产者检查队列是否为满。
    如果不为满，生产者可以继续正常流程。
    如果为满，生产者必须等待，调用condition实例的wait()。
    消费者可以运行。消费者消耗队列，并产生一个空余位置。
    然后消费者notify生产者。
    当消费者释放lock，消费者可以acquire这个lock然后往队列中加入数据。

'''

from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print 'Queue full,producer is waiting'
                condition.wait()
                print 'Space in queue,Consumer notified the producer'
            num = random.choice(nums)
            queue.append(num)
            print 'Produced ', num
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            num = queue.pop(0)
            print 'Consumed', num
            condition.notify()
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
