#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the interfaces of Param Service

"""

import context

# 机器人状态
ROBOT_STATE_STOP = 0
ROBOT_STATE_PAUSE = 1
ROBOT_STATE_EMESTOP = 2
ROBOT_STATE_RUNNING = 3
ROBOT_STATE_ERROR = 4

def get_robot_state(ctx):
    """ 获取机器人状态

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success (int): 机器人状态
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/robot/state")["data"]

# 机器人模式
ROBOT_MODE_TEACH = 0
ROBOT_MODE_PLAY = 1
ROBOT_MODE_REMOTE = 2

def get_robot_mode(ctx):
    """获取机器人模式

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success (int): 机器人模式
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/robot/mode")["data"]

# 机器人模式
ROBOT_MODE = {
    ROBOT_MODE_TEACH: "teach",
    ROBOT_MODE_PLAY: "play",
    ROBOT_MODE_REMOTE: "remote"
}

def set_robot_mode(ctx, mode):
    """设置机器人模式

    Args:
        ctx (context.Context): 登陆上下文
        mode (int): 机器人模式

    Retures:
        Success: True
        Failure: False
    """
    if mode not in ROBOT_MODE:
        return False

    return ctx.tran.put("/v2/paramservice/robot/mode/" + ROBOT_MODE[mode])["success"]

def get_robot_pos(ctx):
    """获取机器人当前位置信息
    Args:
        ctx (context.Context): 登陆上下文

    Retures:
        Success (sequence, 8): 机器人位置
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/robot/pos")["data"]

def get_robot_pose(ctx):
    """获取机器人当前位姿数据
    Args:
        ctx (context.Context): 登陆上下文

    Retures:
        Success (sequence, 8): 机器人位姿
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/robot/pos")["data"]

def get_servo_status(ctx):
    """获取机械臂伺服状态
    Args:
        ctx (context.Context): 登陆上下文

    Retures:
        Success (int): 伺服状态
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/servo/status")["data"]

def get_motor_status(ctx):
    """获取机械臂上下电状态
    Args:
        ctx (context.Context): 登陆上下文

    Retures:
        Success (int): 上下电状态
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/motor/status")["data"]

def get_play_speed(ctx):
    """获取机器人运行速度
    Args:
        ctx (context.Context): 登陆上下文

    Retures:
        Success (int): 机器人运行速度
        Failure (None): None
    """

    return ctx.tran.get("/v2/paramservice/robot/playspeed")["data"]

def set_play_speed(ctx, speed):
    """设置机器人运行速度
    Args:
        ctx (context.Context): 登陆上下文
        speed (int): 机器人运行速度

    Retures:
        Success: True
        Failure: False
    """

    return ctx.tran.put("/v2/paramservice/robot/playspeed/" + str(speed))["success"]