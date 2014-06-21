# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/19
 * Time: 15:30
 * To change this template use File | Settings | File Templates.
'''
from django.db import models

class person(models.Model):
    id = models.IntegerField(max_length=11)
    FirstName =models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
