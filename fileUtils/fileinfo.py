# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-30
# * Time: 上午10:55
# * To change this template use File | Settings | File Templates.
"""Framework for getting filetype-specific metadata.

Instantiate appropriate class with filename.  Returned object acts like a
dictionary, with key-value pairs for each piece of metadata.
    import fileinfo
    info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
    print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

Or use listDirectory function to get info on all files in a directory.
    for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
        ...

Framework can be extended by adding classes for particular file types, e.g.
HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Each class is completely responsible for
parsing its files appropriately; see MP3FileInfo for example.
"""

import os
import sys
from UserDict import UserDict


def stripnulls(data):
    """strip whitespace and nulls"""
    return data.replace("\00", "").strip()


class FileInfo(UserDict):
    """store file metadata"""
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename.decode('gbk').encode('utf-8')


class MP3FileInfo(FileInfo):
    """store ID3V1.0 MP3 tags"""
    tagDataMap = {"title": (3,  44, stripnulls),
                  "artist": (33,  63, stripnulls),
                  "album": (63,  93, stripnulls),
                  "year": (93,  97, stripnulls),
                  "comment": (97, 126, stripnulls),
                  "genre": (127, 128, ord)}

    def __parse(self, filename):
        """parse ID3v1.0 tags from MP3 file """
        # print filename.decode('gbk').encode('utf-8')
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, value):
        if key == "name" and value:
            self.__parse(value)
        FileInfo.__setitem__(self, key, value)


def list_directory(directory, file_ext_list):
    """get list of file info objects for files of particular extensions"""
    file_list = [os.path.normcase(f) for f in os.listdir(directory)]
    file_list = [os.path.join(directory, f) for f in file_list if os.path.splitext(f)[1] in file_ext_list]

    def get_file_info_class(filename, module=sys.modules[FileInfo.__module__]):
        """get file info class from filename extension"""
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

    return [get_file_info_class(f)(f) for f in file_list]


if __name__ == "__main__":
    for infor in list_directory("D:\\QQMusicCache", [".mp3"]):
        print "\n".join(["%s=%s" % (k, v) for k, v in infor.items()])
        print

    print str(stripnulls.__doc__)