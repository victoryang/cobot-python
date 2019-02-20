#!/usr/bin/env python

import context

def get_robot_state(ctx):
    r = ctx.tran.get("/v2/paramservice/robot/state")

    if r[0] != 200:
        print

    return r[1]

def get_robot_mode(ctx):
    r = ctx.tran.get("/v2/paramservice/robot/mode")

    if r[0] != 200:
        print

    return r[1]

def set_robot_mode(ctx, mode):
    r = ctx.tran.put("/v2/paramservice/robot/mode/" + mode)

    if r[0] != 200:
        print False

    return r[1]

def get_robot_pos(ctx):
    r = ctx.tran.get("/v2/paramservice/robot/pos" )

    if r[0] != 200:
        print False

    return r[1]

def get_robot_pose(ctx):
    r = ctx.tran.get("/v2/paramservice/robot/pos")

    if r[0] != 200:
        print False

    return r[1]

def get_servo_status(ctx):
    r = ctx.tran.get("/v2/paramservice/servo/status")

    if r[0] != 200:
        print False

    return r[1]

def get_motor_status(ctx):
    r = ctx.tran.get("/v2/paramservice/motor/status")

    if r[0] != 200:
        print False

    return r[1]

def get_play_speed(ctx):
    r = ctx.tran.get("/v2/paramservice/robot/playspeed")

    if r[0] != 200:
        print False

    return r[1]

def set_play_speed(ctx, speed):
    r = ctx.tran.get("/v2/paramservice/robot/playspeed/" + str(speed))

    if r[0] != 200:
        print False

    return r[1]