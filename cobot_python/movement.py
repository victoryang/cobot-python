#!/usr/bin/env python

import context
import schedule
import param

from threading import Thread

def robot_mode_stop(ctx):
    mode = param.get_robot_mode(ctx)
    if mode == model.ROBOT_STATE_STOP:
        return True

    return False

def joint_move(ctx, target_pos, speed):
    """Run joint move synchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: float: Running speed, 0.5

    Returns:
        Success: True
        Failure: False
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/joint", data)
    if r[0] != 200:
        return False

    sch = schedule.Scheduler(robot_mode_stop, 60)
    return sch.do(ctx)


def cb_example(ret):
    print "ret is " + str(ret)

def joint_move_async(ctx, target_pos, speed, cb=cb_example):
    """Run joint move asynchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: float: Running speed, 0.5
        cb: function: callback function, default cb_example

    Returns:
        Success: True
        Failure: False
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }

    r = ctx.tran.post("/v2/movementservice/robot/movement/joint", data)
    if r[0] != 200:
        return False

    sch = schedule.Scheduler(robot_mode_stop, 60)
    Thread(target=sch.do_async, args=(cb, ctx)).start()

    return r[1]

def set_waypoint_max_joint_speed(ctx, speed):
    """Set max joint speed
    Args:
        ctx: Context
        speed: float: Max joint speed

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/movementservice/robot/movement/waypoints/maxjoinspeed/"+ str(speed))
    if r[0] != 200:
        return False

    return r[1]

def set_waypoint_max_line_speed(ctx, speed):
    """Set max line speed
    Args:
        ctx: Context
        speed: float: Max line speed

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/movementservice/robot/movement/waypoints/maxlinespeed/"+ str(speed))
    if r[0] != 200:
        return False

    return r[1]

def set_waypoint_max_rotate_speed(ctx, speed):
    """Set max rotate speed
    Args:
        ctx: Context
        speed: float: Max rotate speed

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/movementservice/robot/movement/waypoints/maxrotatespeed/"+ str(speed))
    if r[0] != 200:
        return False

    return r[1]

def add_waypoint(ctx, target_pos):
    """Add waypoint info
    Args:
        ctx: Context
        target_pos: float list: Target position

    Returns:
        Success: True
        Failure: False
    """
    data = {
        
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/waypoints", data)
    if r[0] != 200:
        return False

    return r[1]

def clear_waypoint(ctx):
    """Clear waypoint info
    Args:
        ctx: Context

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.delete("/v2/movementservice/robot/movement/waypoints/all")
    if r[0] != 200:
        return False

    return r[1]


def track_move(ctx):
    """Track movement
    Args:
        ctx: Context

    Returns:
        Success: 0
        Failure: False
    """

def stop(ctx):
    """Stop robot
    Args:
        ctx: Context

    Returns:
        Success: 0
        Failure: False
    """
    r = ctx.tran.post("/v2/movementservice/robot/movement/stop")
    if r[0] != 200:
        return False

    return r[1]