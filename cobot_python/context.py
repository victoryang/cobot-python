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

        r = self.tran.post("/v1/login", **kwargs)
        if r[0] != 200:
            print "login fails"
            return

        self.tran.token = r[1]
        print "login success"
        return

    def logout(self):
        if self.is_login():
            self.tran.post("/v1/logout")

        self.tran.token = ""
        self.tran = None

    def check_health(self):
        r = self.tran.get("/health")

        if r[0] != 200:
            print "peer not respond"
            return

        print r[1]