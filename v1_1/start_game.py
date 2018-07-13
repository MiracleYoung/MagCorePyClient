#!/usr/bin/env pythonv2_0
# encoding: utf-8
# @Time    : 2018/7/9 下午4:06
# @Author  : MiracleYoung
# @File    : start_game.py


from v1.app import start_game


# gid = sys.argv[1]
gid = 'f92719bf194247d7913980cde2100387'

game_state = start_game(gid).status_code
# success: 200
print(game_state)
