#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/9 下午4:06
# @Author  : MiracleYoung
# @File    : start_game.py

import sys

from v2_1.game import Game

# gid = sys.argv[1]
gid = sys.argv[1]

game_state = Game(gid).run().status_code
# success: 200
print(game_state)
