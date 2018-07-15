#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午2:40
# @Author  : MiracleYoung
# @File    : app.py

import time
from threading import Thread
import argparse
import random
import string
import sys

from v2_0.attack import Attack
from v2_0.api import API

if __name__ == '__main__':
    letters = string.ascii_letters
    nick = ''.join([random.choice(letters) for _ in range(16)])
    parser = argparse.ArgumentParser(prog='app', description='这是一个MagCore客户端启动器')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
    parser.add_argument('--map', dest='map', type=str, default='RectSmall', help='地图名字。现在有RectSmall,RectMid,RectLarge')
    parser.add_argument('--is_new', dest='is_new', type=str, default='T', choices=['T', 'F'], help='是否创建游戏')
    parser.add_argument('--nick', dest='nick', type=str, default=nick, help='玩家昵称')
    parser.add_argument('--color', dest='color', type=int, choices=range(0, 10), default=0, help='玩家颜色')
    parser.add_argument('--game', dest='game', type=str, default='', help='若不是创建新游戏，请输入游戏id')
    args = parser.parse_args()
    m, nick, is_new, color, gid = args.map, args.nick, args.is_new, args.color, args.game

    if is_new == 'F' and (not gid):
        try:
            sys.exit('若想加入游戏，请输入游戏id： --game 游戏id')
        except Exception as e:
            print(0)

    api = API()
    player = api.reg_player(nick, color)
    pid, bases = player.json()['Id'], player.json()['Bases']

    if is_new == 'T':
        gid = api.new_game(m).text

    print(f'Game id: {gid}')

    if api.join_game(gid, pid).status_code == 200:
        game_state = 0
        while not game_state:
            time.sleep(0.1)
            game = api.get_game(gid).json()
            max, game_state = len(game['Cells']), game['State']
            player = api.get_player(pid).json()
            bx, by = player['Bases'][0].split(',')
            idx = player['Index']
            attack = Attack(gid, pid, api)
        if game_state == 1:
            while True:
                try:
                    owner_cells = attack.get_owner_cells(gid, idx)
                    enemy_bases = attack.get_enemy_bases(idx=idx, game=game)
                    one_enemy_base = enemy_bases.popitem()[1].pop()
                    Thread(target=attack.attack_left, args=(owner_cells, gid, pid, one_enemy_base)).start()
                    Thread(target=attack.attack_right, args=(owner_cells, gid, pid, max, one_enemy_base)).start()
                    Thread(target=attack.attack_up, args=(owner_cells, gid, pid, max, one_enemy_base)).start()
                    Thread(target=attack.attack_down, args=(owner_cells, gid, pid, one_enemy_base)).start()
                except Exception as e:
                    break
