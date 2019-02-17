#!/usr/bin/env python

import transport

class Context(object):
	transport = None

	def __init__(addr, port):
		self.__addr = addr
		self.__port = port
		self.transport = Transport(addr + port)

	def is_login(self):
		return self.transport.token != ""

	def login(self, username, password):
		epwd = base64.urlsafe_b64encode(password)
        url = "/v1/login?username=" + username + "&pwd=" + epwd

		res = self.transport.request("POST", url)
		if res is None:
			print "login fails"
			return

		self.transport.token = res.data
		print "login success"
		return

	def logout():
		if self.is_login():
        	self.transport.request("POST", "/v1/logout")

        self.transport.token = ""
		self.transport = None