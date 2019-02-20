#!/usr/bin/env python

import requests
import requests
import json

DefaultPort = 9000
DefaultTimeOut = 3

class Transport(object):
    token = ""

    def __init__(self, addr):
        self.__addr = addr

    @property
    def addr(self):
        return self.__addr

    @property
    def is_login(self):
        return self.token != ""

    def __url(self, path):
        return self.addr + path

    def __get_standard_header(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        if self.is_login:
            headers["Authorization"] = "bearer " + self.token

        return headers

    def get(self, path):
        r = requests.get(self.__url(path), headers=self.__get_standard_header(), timeout=DefaultTimeOut)

    def post(self, path, data):
        if data is not None:
            data = json.dumps(data)

        r = requests.post(self.__url(path), headers=self.__get_standard_header(), data=data, timeout=DefaultTimeOut)

        try:
            resp = r.json()
        except:
            resp = None

        return r.status_code, resp