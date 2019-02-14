#!/usr/bin/env python

import httplib as http
import json
import base64

DefaultPort = 9000
TimeOut = 3

class Client(object):
    token = ""

    def __init__(self, addr):
        self.__addr = addr
        self.__conn = http.HTTPConnection(addr, DefaultPort, TimeOut)
        print "connectd to: " + addr

    @property
    def addr(self):
        return self.__addr

    def register(self, username, password):
        url = "/v1/login?username=" + username + "&pwd=" + base64.urlsafe_b64encode(password)
        print "url is: " + url
        res = self.sync_request("POST", url)
        if res is not None:
            token = res

    def sync_request(self, method, url, data=None):
        if data is not None:
            data = json.dumps(data)

        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        if self.token != "":
            headers["Authorization"] = "bearer " + self.token

        try:
            self.__conn.request(method, url, data, headers)
        except:
            print "send sync request error"
            return

        try:
            resp = self.__conn.getresponse()
            data = resp.read()
        except:
            print "get response error"
            return

        return json.loads(data)
