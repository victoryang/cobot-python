#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cobot_python import context

ctx = context.Context("192.168.1.253", 9000)

for i in xrange(10):
    ret = ctx.login("Admin", "333333")
    if ret == False:
        print 'login fail at: ' + str(i)
    else:
        print ctx.tran.token

        print "check health: " + str(ctx.check_health())

    ctx.logout()