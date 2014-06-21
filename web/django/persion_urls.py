# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/19
 * Time: 15:38
 * To change this template use File | Settings | File Templates.
'''
from django.conf.urls.defaults import *
import person_views

urlpatterns = patterns('',
    (r'^lastest/$', person_views.lastest_persons),
)
