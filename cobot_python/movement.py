#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the interfaces of Movement Service

"""

import context
import param

def joint_move(ctx, target_pos, speed):
    """关节运动

    Args:
        ctx (context.Context): 登陆上下文
        target_pos (list): 目标关节点, [0,90,0,0,0,0,0,0]
        speed (float): 运行速度百分比，范围:[1~100]，单位：百分比

    Returns:
        Success: True
        Failure: False
    """

    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT
    assert type(speed) == types.FloatType
    assert speed>=1 and speed<=100

    kwargs = {
        "data": {
            "targetPos": target_pos,
            "speed": speed
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/joint", **kwargs)["success"]

def line_move(ctx, target_pos, speed):
    """直线运动

    Args:
        ctx (context.Context): 登陆上下文
        target_pos (list): 目标点, [0,90,0,0,0,0,0,0]
        speed (float): 运行速度，范围[1-3000]，单位：毫米/秒

    Returns:
        Success: True
        Failure: False
    """

    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT
    assert type(speed) == types.FloatType
    assert speed>=1 and speed<=3000

    kwargs = {
        "data": {
            "targetPos": target_pos,
            "speed": speed
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/line", **kwargs)["success"]

def arc_move(ctx, mid_pos, target_pos, speed):
    """圆弧运动, 以机器人当前点作为第一个点，另外给定的两个点构成一个完成圆弧

    Args:
        ctx (context.Context): 登陆上下文
        mid_pos (list): 第二目标点（相对与当前机器人位置）
        target_pos (list): 目标点, [0,90,0,0,0,0,0,0]
        speed (float): 运行速度，范围[1-3000]，单位：毫米/秒

    Returns:
        Success: True
        Failure: False
    """

    assert type(mid_pos) == types.ListType
    assert len(mid_pos) == param.ROBOT_AXIS_COUNT
    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT
    assert type(speed) == types.FloatType
    assert speed>=1 and speed<=3000

    kwargs = {
        "data": {
            "midPos": mid_pos,
            "targetPos": target_pos,
            "speed": speed
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/arc", **kwargs)["success"]

def rotate_move(ctx, target_pos, speed):
    """旋转运动

    Args:
        ctx (context.Context): 登陆上下文
        target_pos (list): 目标点, [0,90,0,0,0,0,0,0]
        speed (float): 运行速度，单位: 度/秒

    Returns:
        Success: True
        Failure: False
    """

    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT
    assert type(speed) == types.FloatType

    kwargs = {
        "data": {
            "targetPos": target_pos,
            "speed": speed
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/arc", **kwargs)["success"]

def set_waypoint_max_joint_speed(ctx, speed):
    """设置多路点运动时最大关节速度

    Args:
        ctx (context.Context): 登陆上下文
        speed (float): 关节速度，范围:[%1~100%], 单位：百分比

    Returns:
        Success: True
        Failure: False
    """

    assert type(speed) == types.FloatType

    return ctx.tran.request("PUT", "/v2/movementservice/robot/movement/waypoints/maxjoinspeed/"+ str(speed))["success"]

def set_waypoint_max_line_speed(ctx, speed):
    """设置多路点运动时最大直线速度

    Args:
        ctx (context.Context): 登陆上下文
        speed (float): 直线速度，范围:[1~3000], 单位：毫米/秒

    Returns:
        Success: True
        Failure: False
    """

    assert type(speed) == types.FloatType
    assert speed >=1 and speed <=3000

    return ctx.tran.request("PUT", "/v2/movementservice/robot/movement/waypoints/maxlinespeed/"+ str(speed))["success"]

def set_waypoint_max_rotate_speed(ctx, speed):
    """设置多路点运动时最大旋转速度

    Args:
        ctx (context.Context): 登陆上下文
        speed (float): 关节速度， 单位：度/秒

    Returns:
        Success: True
        Failure: False
    """

    assert type(speed) == types.FloatType

    return ctx.tran.request("PUT", "/v2/movementservice/robot/movement/waypoints/maxrotatespeed/"+ str(speed))["success"]

def add_waypoint(ctx, target_pos):
    """添加路点信息

    Args:
        ctx (context.Context): 登陆上下文
        target_pos (float list): 目标位置（关节角）

    Returns:
        Success: True
        Failure: False
    """

    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT

    kwargs = {
        "data": {
            "targetPos": target_pos
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/waypoints", **kwargs)["success"]

def clear_waypoint(ctx):
    """清除路点信息

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.request("DELETE", "/v2/movementservice/robot/movement/waypoints/all")["success"]


def track_move(ctx, target_pos, move_type, pl):
    """同步轨迹运动,一次性运行添加的所有路点

    Args:
        ctx (context.Context): 登陆上下文
        target_pos (float list): 目标点，与addWaypoint最后一次调用的目标点相同
        move_type (int): 运动类型（关节、直线、旋转、圆弧）
        pl (int): 平滑度等级，范围[0~7]

    Returns:
        Success: True
        Failure: False
    """

    assert type(target_pos) == types.ListType
    assert len(target_pos) == param.ROBOT_AXIS_COUNT
    assert type(move_type) == types.IntType
    assert type(pl) == types.IntType

    kwargs = {
        "data": {
            "targetPos": target_pos,
            "moveType": move_type,
            "pl": pl
        }
    }

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/rotate", **kwargs)["success"]

def stop(ctx):
    """停止机器人运行

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.request("POST", "/v2/movementservice/robot/movement/stop")["success"]