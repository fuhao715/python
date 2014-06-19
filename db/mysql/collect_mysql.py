# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/19
 * Time: 14:08
 * To change this template use File | Settings | File Templates.
'''
import MySQLdb

def person_list():
    db_comm = MySQLdb.connect(user='root',db='python',passwd='root',host='localhost',charset='utf8')
    cursor = db_comm.cursor()
    cursor.execute('select * from person ')
    names = [row[1] for row in cursor.fetchall()]
    for name in names:
        print name,isinstance(name, str),isinstance(name,  unicode)

    value = [4, '黄', '建']
    cursor.execute('insert into person values(%s, %s, %s)', value)

    cursor.execute('update person set LastName="光" where id=4')

    db_comm.commit()
    cursor.close()
    db_comm.close()

if __name__ == '__main__':
    person_list()