#!/usr/bin/env python

import context

def get_user_list(ctx):
    params = {
        "start": 0,
        "end": 10
    }

    r = ctx.tran.get("/v1/users/", params)
    if r[0] != 200:
        print "get user list fails"

    print "user list: "
    print r[1]["users"]