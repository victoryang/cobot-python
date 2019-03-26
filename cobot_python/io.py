#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the interfaces of IO Service

"""

import context

# IO状态
IO_STATUS_OFF = 0
IO_STATUS_ON = 1

def get_input(ctx, addr):
    """获取输入IO状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输入IO地址

    Returns:
        Success (int): IO状态
        Failure (None): None
    """

    return ctx.tran.request("GET", "/v2/ioservice/io/input/" + str(addr))["data"]

def get_output(ctx, addr):
    """获取输出IO状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输出IO地址

    Returns:
        Success (int): IO状态
        Failure (None): None
    """

    return ctx.tran.request("GET", "/v2/ioservice/io/output/" + str(addr))["data"]

def set_output(ctx, addr, status):
    """设置输出IO状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输出IO地址
        status (int): IO状态

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.request("PUT", "/v2/ioservice/io/output/" + str(addr) + "/" + str(status))["success"]

def get_virtual_input(ctx, addr):
    """获取虚拟IO输入状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输出IO地址

    Returns:
        Success (int): IO状态
        Failure (None): None
    """

    return ctx.tran.request("GET", "/v2/ioservice/io/virtual/input/" + str(addr))["data"]

def get_virtual_output(ctx, addr):
    """获取虚拟IO输出状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输出IO地址

    Returns:
        Success (int): IO状态
        Failure (None): None
    """

    return ctx.tran.request("GET", "/v2/ioservice/io/virtual/output/" + str(addr))["data"]


def set_virtual_output(ctx, addr, status):
    """设置虚拟IO输出状态

    Args:
        ctx (context.Context): 登陆上下文
        addr (int): 输出IO地址
        status (int): IO状态

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.request("PUT", "/v2/ioservice/io/virtual/output/" + str(addr) + "/" + str(status))["success"]

def get_var(ctx, var_name):
    """获取IO总线上的IO变量值

    Args:
        ctx (context.Context): 登陆上下文
        var_name (str): 变量名

    Returns:
        Success (int): 变量值
        Failure (None): None
    """

    return ctx.tran.request("GET", "/v2/ioservice/iobus/vars/" + var_name)["data"]

def set_var(ctx, var_name, value):
    """设置IO总线上的IO变量值

    Args:
        ctx (context.Context): 登陆上下文
        var_name (str): 变量名
        value (int): 变量值

    Returns:
        Success: True
        Failure: False
    """

    return ctx.tran.request("PUT", "/v2/ioservice/iobus/vars/" + var_name + "/" + str(value))["success"]