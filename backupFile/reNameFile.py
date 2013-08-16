__author__ = 'fuhao'
import os
path = 'C:\\Users\\fuhao\\Desktop\\temp'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        newname = file.replace("tmp", "jpg")
        os.rename(os.path.join(path,file),os.path.join(path,newname))
        print(file)