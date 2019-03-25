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
        Success (list): 报警信息列表 [{
            "time": 1551255491,
            "errLevel": 0,
            "errNo": 10001,
            "subErrNo": 0,
            "message": "get arc weld data error"

        }]
        Failure (None): None
    """

    return ctx.tran.get("/v2/alarmservice/alarms/latest")["data"]