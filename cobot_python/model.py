#!/usr/bin/env python

# Robot state code
ROBOT_STATE_STOP = 0
ROBOT_STATE_PAUSE = 1
ROBOT_STATE_EMESTOP = 2
ROBOT_STATE_RUNNING = 3
ROBOT_STATE_ERROR = 4

# Robot mode code, used by get_robot_mode
ROBOT_MODE_TEACH = 0
ROBOT_MODE_PLAY = 1
ROBOT_MODE_REMOTE = 2

# robot mode, used by set_robot_mode
ROBOT_MODE = {
    ROBOT_MODE_TEACH: "teach",
    ROBOT_MODE_PLAY: "play",
    ROBOT_MODE_REMOTE: "remote"
}