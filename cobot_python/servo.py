#!/usr/bin/env python

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
    """Power on servo
    Args:
        ctx: Context

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.post("/v1/robot/axisctrl/sync")["success"]

def startup(ctx):
    """Start servo
    Args:
        ctx: Context

    Returns:
        Success: True
        Failure: False
    """
    data = {
        "args": ["-f"]
    }

    return ctx.tran.post("/v1/robot/axisctrl/servo/on", data)["success"]

def shutdown(ctx):
    """Shut down servo
    Args:
        ctx: Context

    Returns:
        Success: True
        Failure: False
    """
    data = {
        "args": ["-f"]
    }
    
    return ctx.tran.post("/v1/robot/axisctrl/servo/off", data)["success"]