#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/5 下午4:27
# @Author  : MiracleYoung
# @File    : test.py


from concurrent.futures import ThreadPoolExecutor

links = {
    'NEW_GAME': ('http://106.75.33.221:6000/api/game', 'POST'),
    'GET_GAME_LIST': ('http://106.75.33.221:6000/api/game', 'GET'),
    'JOIN_GAME': ('http://106.75.33.221:6000/api/game', 'PATCH'),
    'START_GAME': ('http://106.75.33.221:6000/api/game/', 'PUT'),
    'GET_GAME': ('http://106.75.33.221:6000/api/game/', 'GET'),
    'REG_PLAYER': ('http://106.75.33.221:6000/api/player', 'POST'),
    'GET_PLAYER': ('http://106.75.33.221:6000/api/player/', 'GET'),
    'GET_MAP': ('http://106.75.33.221:6000/api/map/', 'GET'),
    'ATTACK_CELL': ('http://106.75.33.221:6000/api/cell/', 'PUT'),
}

with ThreadPoolExecutor(max_workers=3) as exector:
    f = exector.map()