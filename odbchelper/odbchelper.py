# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-28
# * Time: 下午2:49
# * To change this template use File | Settings | File Templates.
"""odbchelper.py sample script

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.

All this stuff at the top of the script is just optional metadata;
the real code starts on the "def buildConnectionString" line
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 2.7 $"
__date__ = "$Date: 2011/10/28 14:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"


def build_connection_string(params):
    """Build a connection string from a dictionary
    Returns string.
    """
    return ";".join(["%s=%s " % (k, v) for k, v in params.items()])


if __name__ == "__main__":
    myParams = {"server": "mpilgrim",
                "database": "master",
                "uid": "sa",
                "pwd": "secret"}
    print build_connection_string(myParams)
    print build_connection_string.__doc__