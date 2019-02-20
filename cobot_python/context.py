#!/usr/bin/env python

import transport

class Context(object):
    tran = None

    def __init__(addr, port):
        self.__addr = addr
        self.__port = port
        self.tran = transport.Transport(addr + port)

    def is_login(self):
        return self.tran.is_login

    def login(self, username, password):
        epwd = base64.urlsafe_b64encode(password)
        url = "/v1/login?username=" + username + "&pwd=" + epwd

        res = self.tran.post(url, None)
        if res is None:
            print "login fails"
            return

        self.tran.token = res.data
        print "login success"
        return

        def logout():
            if self.is_login():
                self.tran.post("/v1/logout", None)

        self.tran.token = ""
        self.tran = None