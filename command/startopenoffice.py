# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-5
# * Time: 上午10:20
# * To change this template use File | Settings | File Templates.
import subprocess
import re

DEFAULT_OPENOFFICE_PORT = 2002


def find_process():
    p = subprocess.Popen('netstat -lnp|grep ' + str(DEFAULT_OPENOFFICE_PORT), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        process = re.findall(r' \d+\D*$', line)
        if process:
            process_number = process[0].split('/')[0]
            return process_number
    retval = p.wait()
    print p.stdout.read()


def start_soffice():
    ps = subprocess.Popen('nohup soffice --accept="socket,port=2002;urp;" & ', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = ' '
    for line in ps.stdout.readlines():
        out = out + line
    ok = ps.wait()
    # print 'error is %s' % out
    return ok, out

if __name__ == "__main__":
    pid = find_process()
    if pid != None:
        print 'soffice服务已启动：进程号为：%s' % pid
    else:
        print '正在启动soffice服务'
        ok, out = start_soffice()
        if ok == 0:
            pid = find_process()
            if pid != None:
                print 'soffice服务启动成功！进程号为：%s' % pid
            else:
                print 'soffice启动失败! %s' %out

        else:
            print 'soffice启动失败! %s' %out