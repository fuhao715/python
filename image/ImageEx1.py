# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-26
# * Time: 上午8:43
# * To change this template use File | Settings | File Templates.
from PIL import Image

im = Image.open("D:/css123.jpg")
print im.format
print im.size
print im.mode