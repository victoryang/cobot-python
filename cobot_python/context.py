#!/usr/bin/env python

import transport
import base64

class Context(object):
	"""Context Class provide initialization of robot.
    Contains information of robot controller, like communition address information.

    Attributes:
        tran: A transport instance for actual network communication
    """

    tran = None

    def __init__(self, addr, port):
    	"""Init Context with address and port."""
        self.__addr = addr
        self.__port = port
        addr = addr + ":" + str(port)
        self.tran = transport.Transport(addr)

    def is_login(self):
    	"""Check current login status"""
        return self.tran.is_login

    def login(self, username, password):
    	"""Login with username and password.
        Connects to robot controller with username and password.
        Args:
            username: string: username
            password: string: password

        Returns:
            Success: 0
            Failure: Other
        """
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
    	"""To log out."""
        if self.is_login():
            self.tran.post("/v1/logout")

        self.tran.token = ""
        self.tran = None

    def check_health(self):
    	"""Check if robot controller system still works
        Returns:
            Success: 0
            Failure: Other
        """
        r = self.tran.get("/health")

        if r[0] != 200:
            print "peer not respond"
            return

        print r[1]