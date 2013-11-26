# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-26
# * Time: 上午9:55
# * To change this template use File | Settings | File Templates.
import urllib2
import time
from threading import  Thread

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread,self).__init__()

    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()


def get_responses():
    urls = ['http://www.google.com.hk',
            'http://www.baidu.com',
            'http://www.amazon.com',
            'http://www.ebay.com',
            'http://www.alibaba.com',
            'http://www.reddit.com']
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print 'Elapsed time :%s ' % (time.time()-start)

if __name__ == '__main__':
    get_responses()