#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午2:40
# @Author  : MiracleYoung
# @File    : app.py

import time
from threading import Thread

from py_agent.v2.attack import Attack
from py_agent.v2.api import API

if __name__ == '__main__':
    # map_name = sys.argv[1]
    # is_new = sys.argv[2]
    # reg = sys.argv[3]
    # player_name = sys.argv[4]
    # color = sys.argv[5]
    map_name = 'RectSmall'
    is_new = 'new'
    reg = False
    player_name = 'miracleb'
    color = 1

    api = API()
    player = api.get_player('c820b707682246599b8f5499e6fab588') if reg else api.reg_player(player_name, color)
    pid, bases = player.json()['Id'], player.json()['Bases']
    gid = 0

    if is_new == 'new':
        gid = api.new_game().text
    else:
        glst = api.get_game_list().json()
        for g in glst:
            if map_name in g['map']:
                gid = g['id']
                break
    print(f'Game id: {gid}')

    if api.join_game(gid, pid).status_code == 200:
        game_state = 0
        while not game_state:
            time.sleep(0.1)
            game = api.get_game(gid).json()
            max, game_state = len(game['Cells']), game['State']
        if game_state == 1:
            player = api.get_player(pid).json()
            bx, by = player['Bases'][0].split(',')
            idx = player['Index']
            # while is_alive(pid) and has_enemy(gid, idx):
            attack = Attack(gid, pid, api)
            while True:
                try:
                    owner_cells = attack.get_owner_cells(gid, idx)
                    Thread(target=attack.attack_left, args=(owner_cells, gid, pid)).start()
                    Thread(target=attack.attack_right, args=(owner_cells, gid, pid, max)).start()
                    Thread(target=attack.attack_up, args=(owner_cells, gid, pid, max)).start()
                    Thread(target=attack.attack_down, args=(owner_cells, gid, pid)).start()
                except Exception as e:
                    break
