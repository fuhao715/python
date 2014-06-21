# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/19
 * Time: 15:35
 * To change this template use File | Settings | File Templates.
'''
from django.shortcuts import render_to_response
import person_model

def lastest_persons(request):
    person_list = person_model.person.objects.order_by('-id')[:10]
    return render_to_response('last_persons.html',{'person_list':person_list})

