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
    r = ctx.tran.post("/v1/robot/axisctrl/sync")

    if r[0] != 200:
        return False

    return r[1]

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
    r = ctx.tran.post("/v1/robot/axisctrl/servo/on", data)

    if r[0] != 200:
        return False

    return r[1]

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
    r = ctx.tran.post("/v1/robot/axisctrl/servo/off", data)

    if r[0] != 200:
        return False

    return r[1]