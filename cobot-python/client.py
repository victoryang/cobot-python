#!/usr/bin/env python

import http
import json
import base64

DefaultPort = ":9000"

class Client(Object):
    token = ""

    def __init__(self, addr):
        self.__addr = ipaddr
        self.__conn = http.client.HTTPSConnection(addr + DefaultPort)

    @property
    def addr(self):
        return self.__addr

    def register(self, username, password):
        url = self.__addr + "/v1/login?username=" + username + "&pwd=" + base64.urlsafe_b64encode(password)
        self.request("POST", url)

    def request(self, method, url, data):
        if data is not None:
            data = json.dump(data)

        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        if self.token != "":
            headers["Authorization"] = "bearer " + self.token

        self.__conn.request(method, url, data, headers)
        return self.__conn.getresponse()