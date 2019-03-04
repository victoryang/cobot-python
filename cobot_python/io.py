#!/usr/bin/env python

import context

# IO status
IO_STATUS_OFF = 0
IO_STATUS_ON = 1

def get_input(ctx, addr):
    """get input io status
    Args:
        ctx: Context
        addr: int: IO address

    Returns:
        Success: int: IO status
        Failure: False
    """
    r = ctx.tran.get("/v2/ioservice/io/input/" + str(addr))

    if r[0] != 200:
        return False

    return r[1]

def get_output(ctx, addr):
    """get output io status
    Args:
        ctx: Context
        addr: int: IO address

    Returns:
        Success: IO status, see model.py
        Failure: False
    """
    r = ctx.tran.get("/v2/ioservice/io/output/" + str(addr))

    if r[0] != 200:
        return False

    return r[1]

def set_output(ctx, addr, status):
    """set output io status
    Args:
        ctx: Context
        addr: int: IO address
        status: int: IO status

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/ioservice/io/output/" + str(addr) + "/" + str(status))

    if r[0] != 200:
        return False

    return r[1]

def get_virtual_input(ctx, addr):
    """get virtual input io status
    Args:
        ctx: Context
        addr: int: IO address

    Returns:
        Success: IO status, see model.py
        Failure: False
    """
    r = ctx.tran.get("/v2/ioservice/io/virtual/input/" + str(addr))

    if r[0] != 200:
        return False

    return r[1]

def get_virtual_output(ctx, addr):
    """get virtual output io status
    Args:
        ctx: Context
        addr: int: IO address

    Returns:
        Success: IO status, see model.py
        Failure: False
    """
    r = ctx.tran.get("/v2/ioservice/io/virtual/output/" + str(addr))

    if r[0] != 200:
        return False

    return r[1]


def set_virtual_output(ctx, addr, status):
    """set virtual output io status
    Args:
        ctx: Context
        addr: int: IO address
        status: int: IO status

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/ioservice/io/virtual/output/" + str(addr) + "/" + str(status))

    if r[0] != 200:
        return False

    return r[1]

def get_var(ctx, var_name):
    """get iobus variable value
    Args:
        ctx: Context
        var_name: string: Iobus variable name

    Returns:
        Success: Variable value
        Failure: False
    """
    r = ctx.tran.get("/v2/ioservice/iobus/vars/" + var_name)

    if r[0] != 200:
        return False

    return r[1]

def set_var(ctx, var_name, value):
    """set iobus variable value
    Args:
        ctx: Context
        var_name: string: Iobus variable name
        value: int: Iobus variable value

    Returns:
        Success: True
        Failure: False
    """
    r = ctx.tran.put("/v2/ioservice/iobus/vars/" + var_name + "/" + str(value))

    if r[0] != 200:
        return False

    return r[1]