#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This module contains the definition of Object Context.
Context wraps the details for network communication and other
specific infomations that you should not care about.

"""

import transport
import base64

class Context(object):
    """登陆及操作时的上下文

    Attributes:
        tran (transport.Transport): 负责实际的数据传输，保存
            用户信息等信息

    """
    tran = None

    def __init__(self, addr, port):
        """Context's __init__ method

        Args:
            addr (str): 目标机械臂控制系统的IP地址
            port (int): 服务端口号，目前默认9000

        Attributes:
            __addr (str): 目标机械臂控制系统的IP地址
            __port (int): 服务端口号，目前默认9000
        """

        self.__addr = addr
        self.__port = port
        addr = addr + ":" + str(port)
        self.tran = transport.Transport(addr)


    def _is_login(self):
        """检查当前登陆状态"""

        return self.tran.is_login


    def login(self, username, password):
        """登陆控制器系统

        与机器人控制系统建立连接并获得授权

        Args:
            username (str): 登陆用户名
            password (str): 用户密码

        Returns:
            Success: True
            Failure: False
        """

        kwargs = {
            "params": {
                "username": username,
                "pwd": base64.urlsafe_b64encode(password)
            }
        }

        r = self.tran.request("POST","/v1/login", **kwargs)
        if r["success"] == False:
            return False

        self.tran.token = r["data"]
        return True

    def logout(self):
        """退出登陆

        与机器人控制系统建立断开连接并取消授权

        """

        if self._is_login():
            self.tran.request("POST", "/v1/logout")

        self.tran.token = ""

    def __del__(self):
        self.tran = None

    def check_health(self):
        """检查机械臂控制系统健康状态

        Returns:
            Success: True
            Failure: False

        """

        return self.tran.request("GET", "/health")["success"]