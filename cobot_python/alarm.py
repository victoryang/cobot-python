#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""

This module contains the interfaces of Alarm Service

"""

import context

def reset(ctx):
    """复位操作

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.post("/v2/alarmservice/robot/reset")["success"]

def get_latest_alarms(ctx):
    """获取最新的报警信息

    Args:
        ctx (context.Context): 登陆上下文

    Returns:
        Success (dict): 报警信息列表 {
            "time": 1551255491,
            "err_level": 0,
            "err_no": 10001,
            "sub_err_no": 0,
            "message": "get arc weld data error"

        }
        Failure (None): None
    """
    r = ctx.tran.get("/v2/alarmservice/alarms/latest")

    if r["data"] is None:
        return None

    ret = r["data"]
    return {
        "time": ret["time"],
        "err_level": ret["errLevel"],
        "err_no": ret["errNo"],
        "sub_err_no": ret["subErrNo"],
        "message": ret["message"]
    }