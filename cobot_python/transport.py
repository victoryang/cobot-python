#!/usr/bin/env python

import requests
import json

DefaultTimeOut = 3
DefaultSchema = "http://"

class Transport(object):

    token = ""

    def __init__(self, addr):
        self.__addr = DefaultSchema + addr

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

    def __handle_response(self, r):
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

    def __request_common_handle(self, data, kwargs):
        if data:
            kwargs["data"] = json.dumps(data)

        kwargs["headers"] = self.__get_standard_header()
        kwargs["timeout"] = DefaultTimeOut

    def get(self, path, **kwargs):
        self.__request_common_handle(None, kwargs)

        r = requests.get(self.__url(path), **kwargs)

        return self.__handle_response(r)

    def post(self, path, *data, **kwargs):
        self.__request_common_handle(data, kwargs)

        r = requests.post(self.__url(path), **kwargs)

        return self.__handle_response(r)

    def put(self, path, *data, **kwargs):
        self.__request_common_handle(data, kwargs)

        r = requests.put(self.__url(path), **kwargs)

        return self.__handle_response(r)

    def delete(self, path, **kwargs):
        self.__request_common_handle(None, kwargs)

        r = requests.delete(self.__url(path), **kwargs)

        return self.__handle_response(r)