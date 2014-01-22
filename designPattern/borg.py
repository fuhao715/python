# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-1-22
# * Time: 下午4:15
# * To change this template use File | Settings | File Templates.

# 共享模式 borg
class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1:', rm1)
    print('rm2:', rm2)

    rm2.state = 'Zombie'

    print('rm1:', rm1)
    print('rm2:', rm2)

    print('rm1 id:', id(rm1))
    print('rm2 id:', id(rm2))

    rm3 = YourBorg()

    print('rm1:', rm1)
    print('rm2:', rm2)
    print('rm3:', rm3)