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
import sys

COUNTER = 1
mail_server = "smtp.139.com"
mail_port = 25
use_tls = False
mail_username = "15210795193@139.com"
mail_password = "1121ai715"
mail_from = "15210795193@139.com"
mail_to = "15210795193@139.com"
subject_header = None


def send_mail(msg):
    try:
        print 'begin send email !'
        msg = MIMEText(msg.encode(), _charset='utf-8')
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
    except:
        print("send mail fail!")

def monitor(url, price_accpet):
    idx = 0
    timenow = time.strftime("%Y-%m-%d %X", time.localtime())
    while True:
    #for idx in range(COUNTER):
        try:
            page = urllib2.urlopen(url, timeout=1000)
            page = unicode(page.read(),"gb2312","ignore").encode("gb2312","ignore")
            soup = BeautifulSoup(page, fromEncoding="gb18030")
            global subject_header
            subject_header = soup.html.head.title.string
            print subject_header
            subject_header = ''.join(subject_header.encode('utf-8').split('【')[:-1])
            print subject_header
            skuid = url.split('/')[-1].split('.')[0]
            f = urllib2.urlopen('http://p.3.cn/prices/get?skuid=J_'+skuid, timeout=5)
        except Exception,ex:
            print ex
            print "timenow:%s,couldnot open this %s" % (timenow, url)
            continue
        price = json.loads(f.read())
        f.close()
        #print price_promotion
        price_promotion = price[0]['p']
        print price_promotion, price_accpet
        if string.atof(price_promotion) < string.atof(price_accpet):
            send_mail('现降价到'.join(price_promotion))
            break
        time.sleep(60)
    print "program end"

if __name__ == "__main__":
    monitor("http://item.jd.com/934604.html", 9999.00)