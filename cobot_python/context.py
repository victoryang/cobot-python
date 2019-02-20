#!/usr/bin/env python

import transport
import base64

class Context(object):

    tran = None

    def __init__(self, addr, port):
        self.__addr = addr
        self.__port = port
        addr = addr + ":" + str(port)
        self.tran = transport.Transport(addr)

    def is_login(self):
        return self.tran.is_login

    def login(self, username, password):
        kwargs = {
        	"params": {
        		"username": username,
        		"pwd": base64.urlsafe_b64encode(password)
        	}
        }

        res = self.tran.post("/v1/login", kwargs)
        if res[0] != 200:
            print "login fails"
            return

        self.tran.token = res[1]
        print "login success"
        return

    def logout(self):
        if self.is_login():
            self.tran.post("/v1/logout")

        self.tran.token = ""
        self.tran = None