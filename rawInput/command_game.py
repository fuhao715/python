# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-11
# * Time: 下午2:51
# * To change this template use File | Settings | File Templates.
from sys import argv
script, user_name = argv
prompt = '>'

print "Hi %s , I'm the %s script ." % (user_name, script)
print "I'd like to ask you a few questions ."
print "Do you like me %s ? " % user_name
likes = raw_input(prompt)

print "Where are you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print "done "
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
