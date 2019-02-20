#!/usr/bin/env python

import context

def get_user_list(ctx):
    params = {
        "start": 0,
        "end": 10
    }

    res = ctx.tran.get("/v1/users/", params)
    if res[0] != 200:
        print "get user list fails"

    print "user list: "
    print res[1]