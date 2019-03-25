#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cobot_python import context
from cobot_python import param
from cobot_python import servo
from cobot_python import io
from cobot_python import kinematic
from cobot_python import movement
from cobot_python import alarm

ctx = context.Context("192.168.1.253", 9000)

ctx.login("Admin", "333333")

print ctx.tran.token

print "check health: " + str(ctx.check_health())

state = param.get_robot_state(ctx)
print type(state)

print "robot state: " + str(state)

print "power on: " + str(servo.power(ctx))

print "get input status: " + str(io.get_input(ctx, 0))

print "get latest alarm: " + str(alarm.get_latest_alarms(ctx))

ctx.logout()