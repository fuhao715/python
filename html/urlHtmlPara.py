# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-10
# * Time: 上午10:58
# * To change this template use File | Settings | File Templates.
import urllib2
import time
import smtplib
from email.mime.text import MIMEText
from email import utils
import string
import json
from BeautifulSoup import BeautifulSoup
from PIL import Image
import sys


COUNTER = 1
mail_server = "smtp.139.com"
mail_port = 25
use_tls = False
mail_username = "152********@139.com"
mail_password = "******"
mail_from = "152********@139.com"
mail_to = "186********@139.com"
subject_header = None


def send_mail(msg):
    try:
        print 'begin send email !'
        msg = MIMEText(msg)
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = subject_header
        msg['Date'] = utils.formatdate(localtime=1)
        mailServer = smtplib.SMTP(mail_server, mail_port)
        if use_tls:
            mailServer.starttls()
        mailServer.login(mail_username, mail_password)
        mailServer.sendmail(mail_from, mail_to, msg.as_string())
        mailServer.close()
        print 'end send email'
    except Exception, ex:
        print ex, 'send mail fail!'


def monitor(url, price_accpet):
    idx = 0
    timenow = time.strftime("%Y-%m-%d %X", time.localtime())
    while True:
    #for idx in range(COUNTER):
        try:
            page = urllib2.urlopen(url, timeout=1000)
            page = unicode(page.read(), "gb2312", "ignore").encode("gb2312", "ignore")
            soup = BeautifulSoup(page, fromEncoding="gb18030")
            global subject_header
            subject_header = soup.html.head.title.string
            print subject_header
            subject_header = ''.join(subject_header.encode('utf-8').split('【')[:-1])
            print subject_header
            skuid = url.split('/')[-1].split('.')[0]
            f = urllib2.urlopen('http://p.3.cn/prices/get?skuid=J_'+skuid, timeout=5)
        except Exception, ex:
            print ex, 'timenow:%s,couldnot open this %s' % (timenow, url)
            continue
        price = json.loads(f.read())
        f.close()
        #print price_promotion
        price_promotion = price[0]['p']
        print price_promotion, price_accpet
        if string.atof(price_promotion) < string.atof(price_accpet):
            message = ''.join(['价格降低到 ', (price_promotion.encode('utf-8'))])
            subject_header = ''.join([subject_header, message])
            print subject_header, '----', message
            send_mail(message)
            break
        time.sleep(60)
    print "program end"


#图像数字识别
class PriceReco:
    img_data = []
    size_x, size_y = 0, 0
    def __init__(self, filename):  #加载变换图片
        try:
            img = Image.open(filename)
        except:
            print filename, "load error"
            return
        self.size_x, self.size_y = img.size
        self.img_data = list(img.convert('L').getdata())
        for i in range(0, len(self.img_data)):
            self.img_data[i] = 255 - self.img_data[i]
        #print filename, "load success, image size is", self.size_x, self.size_y
        #print self.img_data

    def getone(self, single): #识别单个数字
        table_value = [
                [189, 378, 945, 1512, 2079, 1701, 1701, 1134, 945, 378, 189], #￥
                [567, 567], # .
                [1323, 1701, 756, 378, 378, 378, 756, 1701, 1323], # 0
                [378, 378, 2079, 2079, 189, 189], # 1
                [567, 945, 756, 756, 756, 756, 945, 945, 567], # 2
                [756, 1134, 378, 567, 567, 567, 1323, 1512, 756], # 3
                [378, 378, 378, 378, 378, 378, 2079, 2079, 189, 189], # 4
                [378, 1512, 1134, 567, 567, 567, 945, 1134, 756], # 5
                [1134, 1512, 945, 756, 567, 567, 945, 1134, 567], # 6
                [189, 189, 378, 756, 945, 945, 945, 756, 378], # 7
                [756, 1512, 1323, 567, 567, 567, 1323, 1512, 756], # 8
                [567, 1134, 945, 567, 567, 756, 945, 1512, 1134], # 9
                ]
        table_key = ['￥', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        key_id, min_value = 0, 100000
        #print single
        for k in range(0, len(table_key)):
            #print len(table_value[k]), len(single)
            value = 10 * (len(table_value[k]) - len(single)) ** 2
            #print value
            for i in range(0, min(len(table_value[k]), len(single))):
                value += (table_value[k][i] - single[i]) ** 2
            #print value
            if value < min_value:
                key_id, min_value = k, value
                #print "updata: ", key_id, min_value
        #print min_value
        if min_value > 100:
            return 'N'
        else:
            return table_key[key_id]

    def recognita(self): #切分和识别图片
        cnt = [0] * self.size_x
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                index = y * self.size_x + x
                cnt[x] += self.img_data[index]
        #print cnt
        x = 0
        number = ""
        while x < self.size_x:
            if cnt[x]:
                single = []
                while x < self.size_x and cnt[x]:
                    single.append(cnt[x])
                    x += 1
                number += self.getone(single)
            x += 1
        return number


if __name__ == "__main__":
    price = PriceReco('D:/a.jpg')
    print price.recognita()
    # monitor("http://item.jd.com/934604.html", 9999.00)

