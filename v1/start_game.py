#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/9 下午4:06
# @Author  : MiracleYoung
# @File    : start_game.py


import sys
from py_agent.v1.app import start_game


# gid = sys.argv[1]
gid = 'df373aa7caa949dc83e854f829691b56'

game_state = start_game(gid).status_code
# success: 200
print(game_state)
