# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-11-26
# * Time: 上午8:43
# * To change this template use File | Settings | File Templates.
# 学习网址 http://pillow.readthedocs.org/en/latest/handbook/tutorial.html
from PIL import Image
from multiprocessing import Pool
import os

ims = Image.open("D:/css/css123.jpg")
print ims.format
print ims.size
print ims.mode

SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'

## 遍历目录并获取文件类型为jpg的文件
def get_image_paths(folder):
    return (os.path.join(folder, f) for f in os.listdir(folder) if 'jpg' in f)

## 创建文件缩略图
def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)

if __name__ == '__main__':
    folder = os.path.abspath('D:/css/')
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

    images = get_image_paths(folder)

    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()


