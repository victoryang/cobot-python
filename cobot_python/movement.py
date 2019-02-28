#!/usr/bin/env python

import context
import schedule
import param

from threading import Thread

def robot_state_stop(ctx):
    state = param.get_robot_state(ctx)
    if state == param.ROBOT_STATE_STOP or state == param.ROBOT_STATE_ERROR:
        return True

    return False

def do_movement_check(ctx, target_pos):
    sch = schedule.Scheduler(robot_state_stop, 60)

    if sch.do(ctx):
        pos = get_robot_pos(ctx)
        if set(pos) == set(target_pos):
            return 0
        else:
            if param.get_robot_state(ctx) == param.ROBOT_STATE_ERROR:
                return -2
            else:
                return -1

    return -3

def cb_example(ret):
    print "ret is " + str(ret)

def do_movement_check_async(ctx, target_pos, cb=cb_example):
    ret = do_movement_check(ctx, target_pos)
    cb(ret)

def joint_move(ctx, target_pos, speed):
    """Run joint move synchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: float: Running speed, 0.5

    Returns:
        Success: 0
        Failure: Other
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/joint", data)
    if r[0] != 200:
        return False

    return do_movement_check(ctx, target_pos)

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

    Thread(target=do_movement_check_async, args=(ctx, target_pos, cb)).start()

    return r[1]

def line_move(ctx, target_pos, speed):
    """Run line move synchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: int: Running speed, [1-3000]

    Returns:
        Success: 0
        Failure: Other
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/line", data)
    if r[0] != 200:
        return False

    return do_move_check(ctx, target_pos)

def line_move_async(ctx, target_pos, speed, cb=cb_example):
    """Run line move asynchronously
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

    r = ctx.tran.post("/v2/movementservice/robot/movement/line", data)
    if r[0] != 200:
        return False

    Thread(target=do_movement_check_async, args=(ctx, target_pos, cb)).start()

    return r[1]

def arc_move(ctx, mid_pos, target_pos, speed):
    """Run arc move synchronously
    Args:
        ctx: Context
        mid_pos: list: 
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: int: Running speed, [1-3000]

    Returns:
        Success: 0
        Failure: Other
    """
    data = {
        "midPos": mid_pos,
        "targetPos": target_pos,
        "speed": speed
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/arc", data)
    if r[0] != 200:
        return False

    return do_move_check(ctx, target_pos)

def rotate_move(ctx, target_pos, speed):
    """Run rotate move synchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: int: Running speed

    Returns:
        Success: 0
        Failure: Other
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }
    r = ctx.tran.post("/v2/movementservice/robot/movement/rotate", data)
    if r[0] != 200:
        return False

    return do_move_check(ctx, target_pos)

def rotate_move_async(ctx, target_pos, speed, cb=cb_example):
    """Run rotate move asynchronously
    Args:
        ctx: Context
        target_pos: list: target position, [0,90,0,0,0,0,0,0]
        speed: float: Running speed
        cb: function: callback function, default cb_example

    Returns:
        Success: True
        Failure: False
    """
    data = {
        "targetPos": target_pos,
        "speed": speed
    }

    r = ctx.tran.post("/v2/movementservice/robot/movement/line", data)
    if r[0] != 200:
        return False

    Thread(target=do_movement_check_async, args=(ctx, target_pos, cb)).start()

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