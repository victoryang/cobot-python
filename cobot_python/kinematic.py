#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the interfaces of Kinematics Service

"""

import context

def inverse_kinematic(ctx, pose):
    """逆解函数，根据位姿信息得到对应的机械臂关节角信息

    Args:
        ctx (context.Context): 登陆上下文
        pose (list): 位姿信息

    Returns:
        Success (list): 关节角信息
        Failure (None): None
    """

    kwargs = {
        "data": {
            "pose": pose
        }
    }

    return ctx.tran.request("POST", "/v2/kinematicsservice/inversekinematic", **kwargs)["data"]

def positive_kinematic(ctx, pos):
    """正解函数，根据机械臂关节角信息得到对应的位姿信息

    Args:
        ctx (context.Context): 登陆上下文
        pos (list): 关节角信息

    Returns:
        Success (list): 位姿信息
        Failure (None): None
    """

    kwargs = {
        "data": {
            "pose": pos
        }
    }

    return ctx.tran.request("POST", "/v2/kinematicsservice/positivekinematic", **kwargs)["data"]

def base2user(ctx, pose, user_no=-1):
    """基坐标到用户坐标位姿转化函数，当前用户坐标系下，根据基坐标的位姿信息得到对应用户坐标系下的位姿信息

    Args:
        ctx (context.Context): 登陆上下文
        pose (list): 基坐标系下的位姿信息
        user_no (int, optional): 用户坐标号，指向用户坐标系

    Returns:
        Success (list): 用户坐标系下的位姿信息
        Failure (None): None
    """

    kwargs = {
        "data": {
            "pose": pose,
            "userNo": user_no
        }
    }

    return ctx.tran.request("POST", "/v2/kinematicsservice/base2user", **kwargs)["data"]

def user2base(ctx, pose, user_no=-1):
    """用户坐标到基坐标位姿转化，当前用户坐标系下，根据用户坐标的位姿信息得到对应基坐标系下的位姿信息

    Args:
        ctx (context.Context): 登陆上下文
        pose (list): 用户坐标系下的位姿信息
        user_no (int, optional): 用户坐标号，指向用户坐标系

    Returns:
        Success (list): 基坐标系下的位姿信息
        Failure (None): None
    """

    kwargs = {
        "data": {
            "pose": pose,
            "userNo": user_no
        }
    }

    return ctx.tran.request("POST", "/v2/kinematicsservice/base2user", **kwargs)["data"]