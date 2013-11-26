# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-26
# * Time: 上午9:50
# * To change this template use File | Settings | File Templates.
import time
import urllib2


def get_responses():
    urls = ['http://www.google.com.hk',
            'http://www.baidu.com',
            'http://www.amazon.com',
            'http://www.ebay.com',
            'http://www.alibaba.com',
            'http://www.reddit.com']
    start = time.time()
    for url in urls:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()

    print 'Elapsed time :%s ' % (time.time()-start)

if __name__ == '__main__':
    get_responses()
