# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-5
# * Time: 上午10:20
# * To change this template use File | Settings | File Templates.
import subprocess
import re
import traceback
import tempfile
import time
import os
import logging
import logging.handlers

DEFAULT_OPENOFFICE_PORT = 2002


def find_process():
    p = subprocess.Popen('netstat -lnp|grep ' + str(DEFAULT_OPENOFFICE_PORT), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    for line in p.stdout.readlines():
        process = re.findall(r' \d+\D*$', line)
        if process:
            process_number = process[0].split('/')[0]
            return process_number
    print p.stdout.read()


def start_soffice():
    try:
        out_temp = tempfile.SpooledTemporaryFile(bufsize=10*1000)
        fileno = out_temp.fileno()
        ps = subprocess.Popen('nohup soffice --accept="socket,port=2002;urp;" & ', stdout=fileno, stderr=fileno, shell=True )
        ok = ps.wait()
        out_temp.seek(0)
        lines = out_temp.readlines()
        print lines

        print ps.pid
        return ok, lines
    except Exception, e:
            print traceback.format_exc()
    finally:
            if out_temp:
                        out_temp.close()


if __name__ == "__main__":
    log_file = os.path.join(os.getcwd(), 'dzda.log')
    my_log = logging.getLogger("MyLogger")
    my_log.setLevel(logging.DEBUG)

    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    my_log.addHandler(handler)
    pid = find_process()
    if pid != None:
        my_log.debug('soffice服务已启动：进程号为：%s', pid)
    else:
        my_log.debug('正在启动soffice服务')
        ok, out = start_soffice()
        if ok == 0:
            time.sleep(5)
            pid = find_process()
            if pid != None:
                my_log.debug('soffice服务启动成功！进程号为：%s', pid)
            else:
                my_log.debug('soffice启动失败! %s', out)

        else:
            my_log.debug('soffice启动失败! %s', out)