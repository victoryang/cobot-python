#!/usr/bin/env python

import requests
import json

DefaultTimeOut = 3
DefaultSchema = "http://"

def url(addr, path):
    return DefaultSchema + addr + path

def request_common_handle(token, kwargs):
    if "data" in kwargs:
        kwargs["data"] = json.dumps(kwargs["data"])

    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    if token:
        headers["Authorization"] = "bearer " + token
            
    kwargs["headers"] = headers
    kwargs["timeout"] = DefaultTimeOut

def handle_response(r):
    try:
        resp = r.json()
    except:
        resp = None

    if r.status_code == 200:
        return {
            "success": True,
            "data": resp,
            "ecode": 0,
            "emsg": "",
        }

    return {
        "success": False,
        "data": None,
        "ecode": r.status_code,
        "emsg": "request error",
    }

class Transport(object):

    _token = ""

    def __init__(self, addr):
        self.__addr = addr

    @property
    def addr(self):
        return self.__addr

    @property
    def is_login(self):
        return self._token != ""

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, val):
        self._token = val

    def request(self, method, path, **kwargs):

        request_common_handle(self.token, kwargs)

        return handle_response(requests.request(method, url(self.addr, path), **kwargs))