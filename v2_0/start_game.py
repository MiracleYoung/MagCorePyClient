#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/9 下午4:06
# @Author  : MiracleYoung
# @File    : start_game.py


from v2_0.game import Game

# gid = sys.argv[1]
gid = 'abe3adb17bf04ac4b66b21e601b2cedf'

game_state = Game(gid).run().status_code
# success: 200
print(game_state)
