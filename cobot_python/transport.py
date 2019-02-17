#!/usr/bin/env python

import httplib as http
import json
import base64

DefaultPort = 9000
TimeOut = 3

class Transport(object):
    token = ""

    def __init__(self, addr):
        self.__addr = addr

    @property
    def addr(self):
        return self.__addr

    def request(self, method, url, data=None):
        if data is not None:
            data = json.dumps(data)

        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        if self.token != "":
            headers["Authorization"] = "bearer " + self.token

        try:
            conn = http.HTTPConnection(addr, DefaultPort, TimeOut)
            conn.request(method, url, data, headers)
        except http.NotConnected:
            print "Lost connection, please retry"
        except:
            print "send sync request error"
            return

        try:
            resp = self.__conn.getresponse()
            data = resp.read()
        except:
            print "get response error"
            return

        if resp.status != 200:
            print "response fails: " + resp.reason
            return

        return {
            data:json.loads(data)
        }