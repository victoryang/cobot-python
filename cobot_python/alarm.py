#!/usr/bin/env python

import context

def reset(ctx):
    """Reset alarm info
    Args:
        ctx: Context

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.post("/v2/alarmservice/robot/reset")
    if r[0] != 200:
        return False

    return r[1]

def get_latest_alarms(ctx):
    """Get latest alarm info
    Args:
        ctx: Context

    Returns:
        Success: dict or None: {
            "time": 1551255491,
            "err_level": 0,
            "err_no": 10001,
            "sub_err_no": 0,
            "message": "get arc weld data error"

        }
        Failure: False
    """
    r = ctx.tran.get("/v2/alarmservice/alarms/latest")
    if r[0] != 200:
        return False

    if r[1] is None:
        return None

    ret = r[1]
    return {
        "time": ret["time"],
        "err_level": ret["errLevel"],
        "err_no": ret["errNo"],
        "sub_err_no": ret["subErrNo"],
        "message": ret["message"]
    }