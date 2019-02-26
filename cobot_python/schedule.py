#!/usr/bin/env python

import time

class Scheduler(object):

    def __init__(task, timeout):
        self.task = task
        self.timeout = timeout

    def generator(self, *args):
        loop = yield True
        while loop:
            time.sleep(1)
            resp = self.task(*args)
            loop = yield resp

    def do(self, *args):
        i = 0
        g = self.generator(*args)
        g.next()

        while i < self.timeout:
            i = i + 1
            r = g.send(True)
            if r == True:
                break

        g.close()

        if i == self.timeout:
            return False

        return True