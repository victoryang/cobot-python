#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the interfaces of Servo Service

"""

import context

def get_user_list(ctx):
    kwargs = {
        "params": {
            "start": 0,
            "end": 10
        }
    }

    r = ctx.tran.get("/v1/users/", **kwargs)
    if r[0] != 200:
        print "get user list fails"

    print "user list: "
    print r[1]["users"]

def power(ctx):
    """伺服系统上下电

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.post("/v1/robot/axisctrl/sync")["success"]

def startup(ctx):
    """启动伺服

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    data = {
        "args": ["-f"]
    }

    return ctx.tran.post("/v1/robot/axisctrl/servo/on", data)["success"]

def shutdown(ctx):
    """关闭伺服
    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    data = {
        "args": ["-f"]
    }

    return ctx.tran.post("/v1/robot/axisctrl/servo/off", data)["success"]