__author__ = 'fuhao'
# -*- coding: UTF-8 -*-
import hashlib
import sys
import os


def Usage(argv):
    print("usage : {0} folder1 folder2".format(argv[0]))

def CalculateFileHash(file):
    f = open(file, "rb")
    content = f.read()
    m = hashlib.md5()
    #m = hashlib.sha1()
    m.update(content)
    s = m.hexdigest()
    del m
    f.close()
    return s

class HashFile:
    def __init__(self, file_path):
        self.Load(file_path)

    def Load(self, file_path):
        self.file_ext = file_path[file_path.rfind("."):]
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_size = os.path.getsize(file_path)
        self.hash_code = CalculateFileHash(file_path)

    def Equal(self, other):
        if self.file_size != other.file_size:
            return 0
        elif self.hash_code != other.hash_code:
            return 0
        else:
            return 1

def FolderToDict(folder):
    file_dict = {}
    for root, dirs, files in os.walk(folder): #ignore subdirectories here
        for file in files:
            path=os.path.join(root, file)
            file_dict[path] = HashFile(path)
    return file_dict

def CompareTwoFolder(src, dst):
    src_dict = FolderToDict(src)
    dst_dict = FolderToDict(dst)
    for skey, sval in src_dict.items():
        for dkey, dval in dst_dict.items():
            if sval.Equal(dval):
                print('file "{0}" and "{1}" are identical'.format(skey, dkey))
                #todo : delete one file here
                break


def recursiveOneFolder(folder_name):
    file_dict = []
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            path = os.path.join(root, f)
            hashFile = HashFile(path)
            ist = [x for x in file_dict if hashFile.Equal(x)]
            if len(ist) != 0:
                print('file "{0}" is exist {1} '.format(path, ist[0].file_path))
            else:
                    file_dict.append(hashFile)


if __name__ == '__main__':
    #CompareTwoFolder('D:\\book', 'D:\\book1')
    #sys.exit()
    recursiveOneFolder('D:/temp/test/')


'''
    if (len(sys.argv) < 3):
        Usage(sys.argv)
        sys.exit()
    else:
        CompareTwoFolder(sys.argv[1], sys.argv[2])
        sys.exit()
'''
