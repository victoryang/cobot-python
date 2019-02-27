#!/usr/bin/env python

import context
import model

# Robot state code
ROBOT_STATE_STOP = 0
ROBOT_STATE_PAUSE = 1
ROBOT_STATE_EMESTOP = 2
ROBOT_STATE_RUNNING = 3
ROBOT_STATE_ERROR = 4

def get_robot_state(ctx):
    """Get robot state
    Args:
        ctx: Context

    Returns:
        Success: int: robot state code
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/robot/state")

    if r[0] != 200:
        return False

    return r[1]

# Robot mode code
ROBOT_MODE_TEACH = 0
ROBOT_MODE_PLAY = 1
ROBOT_MODE_REMOTE = 2

def get_robot_mode(ctx):
    """Get robot mode
    Args:
        ctx: Context

    Returns:
        Success: int: robot mode code
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/robot/mode")

    if r[0] != 200:
        return False

    return r[1]

# Robot mode map
ROBOT_MODE = {
    ROBOT_MODE_TEACH: "teach",
    ROBOT_MODE_PLAY: "play",
    ROBOT_MODE_REMOTE: "remote"
}

def set_robot_mode(ctx, mode):
    """Set robot mode
    Args:
        ctx: Context
        mode: int: robot mode code

    Retures:
        Success: True
        Failure: False
    """
    if mode is not in model.ROBOT_MODE:
        return False

    r = ctx.tran.put("/v2/paramservice/robot/mode/" + model.ROBOT_MODE[mode])

    if r[0] != 200:
        return False

    return r[1]

def get_robot_pos(ctx):
    """Get robot position
    Args:
        ctx: Context

    Retures:
        Success: Robot pos, [0,90,0,0,0,0,0,0]
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/robot/pos")

    if r[0] != 200:
        print False

    return r[1]

def get_robot_pose(ctx):
    """Get robot pose
    Args:
        ctx: Context

    Retures:
        Success: Robot pos, [0,0,0,0,0,0]
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/robot/pos")

    if r[0] != 200:
        print False

    return r[1]

def get_servo_status(ctx):
    """Get servo status
    Args:
        ctx: Context

    Retures:
        Success: True
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/servo/status")

    if r[0] != 200:
        print False

    return r[1]

def get_motor_status(ctx):
    """Get motor status
    Args:
        ctx: Context

    Retures:
        Success: True
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/motor/status")

    if r[0] != 200:
        print False

    return r[1]

def get_play_speed(ctx):
    """Get robot play speed info
    Args:
        ctx: Context

    Retures:
        Success: speed, type int
        Failure: False
    """
    r = ctx.tran.get("/v2/paramservice/robot/playspeed")

    if r[0] != 200:
        print False

    return r[1]

def set_play_speed(ctx, speed):
    """Set robot play speed
    Args:
        ctx: Context
        speed: int: play speed

    Retures:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/paramservice/robot/playspeed/" + str(speed))

    if r[0] != 200:
        print False

    return r[1]