#!/usr/bin/env python

import context

def inverse_kinematic(ctx, pose):
    """inverse kinematic function
    Args:
        ctx: Context
        pose: list: pose info

    Returns:
        Success: list: Pose info
        Failure: False
    """
    r = ctx.tran.post("/v2/kinematicsservice/inversekinematic", pose)
    if r[0] != 200:
        return False

    return r[1]

def positive_kinematic(ctx, pos):
    """positive kinematic function
    Args:
        ctx: Context
        pos: list: pos info

    Returns:
        Success: list: Pos info
        Failure: False
    """
    r = ctx.tran.post("/v2/kinematicsservice/positivekinematic", pose)
    if r[0] != 200:
        return False

    return r[1]

def base2user(ctx, pose, user_no=-1):
    """positive kinematic function
    Args:
        ctx: Context
        pose: list: pose info

    Returns:
        Success: list: Pose info
        Failure: False
    """
    data = {
        "pose": pose,
        "userNo": user_no
    }
    r = ctx.tran.post("/v2/kinematicsservice/base2user", data)
    if r[0] != 200:
        return False

    return r[1]

def user2base(ctx, pose, user_no=-1):
    """positive kinematic function
    Args:
        ctx: Context
        pose: list: pose info

    Returns:
        Success: list: Pose info
        Failure: False
    """
    data = {
        "pose": pose,
        "userNo": user_no
    }
    r = ctx.tran.post("/v2/kinematicsservice/base2user", data)
    if r[0] != 200:
        return False

    return r[1]