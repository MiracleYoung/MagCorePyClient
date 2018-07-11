#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午2:40
# @Author  : MiracleYoung
# @File    : app.py

HEADER = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache'
}

NEW_GAME = ('http://106.75.33.221:6000/api/game', 'POST')
GET_GAME_LIST = ('http://106.75.33.221:6000/api/game', 'GET')
JOIN_GAME = ('http://106.75.33.221:6000/api/game', 'PATCH')
START_GAME = ('http://106.75.33.221:6000/api/game/', 'PUT')
GET_GAME = ('http://106.75.33.221:6000/api/game/', 'GET')

REG_PLAYER = ('http://106.75.33.221:6000/api/player', 'POST')
GET_PLAYER = ('http://106.75.33.221:6000/api/player/', 'GET')

GET_MAP = ('http://106.75.33.221:6000/api/map/', 'GET')

ATTACK_CELL = ('http://106.75.33.221:6000/api/cell/', 'PUT')

import requests, pprint, sys, time, random


def new_game():
    payload = {
        'Map': 'RectSmall'
    }
    res = requests.request(NEW_GAME[1], NEW_GAME[0], json=payload, headers=HEADER)
    pprint.pprint(f'New game: {res.text}')
    return res


def get_game_list():
    res = requests.request(GET_GAME_LIST[1], GET_GAME_LIST[0], headers=HEADER)
    pprint.pprint(f'games list: {res.text}')
    return res


def join_game(gid, pid):
    payload = {
        'Game': gid,
        'Player': pid
    }
    res = requests.request(JOIN_GAME[1], JOIN_GAME[0], json=payload, headers=HEADER)
    return res


def start_game(gid):
    res = requests.request(START_GAME[1], START_GAME[0] + gid, headers=HEADER)
    pprint.pprint(f'Start game {gid}: {res}')
    return res


def get_game(gid):
    res = requests.request(GET_GAME[1], GET_GAME[0] + gid, headers=HEADER)
    pprint.pprint(f'Get game {gid}: {res.status_code}')
    return res


def reg_player(name, cid):
    payload = {
        'Name': name,
        'Color': cid
    }
    res = requests.request(REG_PLAYER[1], REG_PLAYER[0], json=payload, headers=HEADER)
    pprint.pprint(f'Register player {name}: {res.json()["Id"]}')
    return res


def get_player(pid):
    res = requests.request(GET_PLAYER[1], GET_PLAYER[0] + pid, headers=HEADER)
    pprint.pprint(f'Get player {pid}')
    return res


def get_map(map_name):
    res = requests.request(GET_MAP[1], GET_MAP[0] + map_name, headers=HEADER)
    pprint.pprint(f'Get map {map_name}')
    return res


def attack_cell(gid, pid, x, y):
    payload = {
        "Game": gid,
        "Player": pid,
        "X": x,
        "Y": y
    }
    res = requests.request(ATTACK_CELL[1], ATTACK_CELL[0], json=payload, headers=HEADER)
    pprint.pprint(f'Attack cell <{x}, {y}>')
    return res


def get_owner_cells(gid, idx):
    cells = get_game(gid).json()['Cells']
    return [[i, j] for i, row in enumerate(cells) for j, cell in enumerate(row) if cell['Owner'] == idx]


def is_alive(pid):
    return get_player(pid).json()['State'] == 1


def has_enemy(gid, idx):
    try:
        cells = get_game(gid).json()['Cells']
        for i, row in enumerate(cells):
            for j, cell in enumerate(row):
                if cell['Owner'] not in (idx, 0):
                    return True
    except:
        pass
    finally:
        return False


def attack(owner_cells, gid, pid, max):
    for x, y in owner_cells:
        if [x, y + 1] not in owner_cells and y + 1 < max:
            attack_cell(gid, pid, y + 1, x)
        if [x, y - 1] not in owner_cells and y - 1 >= 0:
            attack_cell(gid, pid, y - 1, x)
        if [x + 1, y] not in owner_cells and x + 1 < max:
            attack_cell(gid, pid, y, x + 1)
        if [x - 1, y] not in owner_cells and x - 1 >= 0:
            attack_cell(gid, pid, y, x - 1)


if __name__ == '__main__':
    # map_name = sys.argv[1]
    # is_new = sys.argv[2]
    # reg = sys.argv[3]
    # player_name = sys.argv[4]
    # color = sys.argv[5]
    map_name = 'RectSmall'
    is_new = 'new'
    reg = False
    player_name = 'cc'
    color = 1


    # 'c67354586ce049d5bf93fe52b2f3fcc9'
    player = get_player('c820b707682246599b8f5499e6fab588') if reg else reg_player(player_name, color)
    pid, bases = player.json()['Id'], player.json()['Bases']
    gid = ""

    if is_new == 'new':
        gid = new_game().text
    else:
        glst = get_game_list().json()
        for g in glst:
            if map_name in g['map']:
                gid = g['id']
                break
    #gid = "55ab98d462ad4bfcbec9faef1a4fec98"
    print(f'Game id: {gid}')

    if join_game(gid, pid).status_code == 200:
        game_state = 0
        while not game_state:
            time.sleep(0.1)
            game = get_game(gid).json()
            max, game_state = len(game['Cells']), game['State']
        if game_state == 1:
            player = get_player(pid).json()
            bx, by = player['Bases'][0].split(',')
            idx = player['Index']
            # while is_alive(pid) and has_enemy(gid, idx):
            while True:
                try:
                    owner_cells = get_owner_cells(gid, idx)
                    attack(owner_cells, gid, pid, max)
                except Exception as e:
                    break
