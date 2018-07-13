#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/10 下午8:53
# @Author  : MiracleYoung
# @File    : api.py

from requests import request


class API:
    def __init__(self):
        self._links = {
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
        self._headers = {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }

    def new_game(self):
        payload = {
            'Map': 'RectSmall'
        }
        res = request(self._links['NEW_GAME'][1], self._links['NEW_GAME'][0], json=payload, headers=self._headers)
        print(f'New game: {res.text}')
        return res

    def get_game_list(self):
        res = request(self._links['GET_GAME_LIST'][1], self._links['GET_GAME_LIST'][0], headers=self._headers)
        print(f'games list: {res.text}')
        return res

    def join_game(self, gid, pid):
        payload = {
            'Game': gid,
            'Player': pid
        }
        res = request(self._links['JOIN_GAME'][1], self._links['JOIN_GAME'][0], json=payload, headers=self._headers)
        return res

    def start_game(self, gid):
        res = request(self._links['START_GAME'][1], self._links['START_GAME'][0] + gid, headers=self._headers)
        print(f'Start game {gid}: {res}')
        return res

    def get_game(self, gid):
        res = request(self._links['GET_GAME'][1], self._links['GET_GAME'][0] + gid, headers=self._headers)
        print(f'Get game {gid}: {res.status_code}')
        return res

    def reg_player(self, name, cid):
        payload = {
            'Name': name,
            'Color': cid
        }
        res = request(self._links['REG_PLAYER'][1], self._links['REG_PLAYER'][0], json=payload, headers=self._headers)
        print(f'Register player {name}: {res.json()["Id"]}')
        return res

    def get_player(self, pid):
        res = request(self._links['GET_PLAYER'][1], self._links['GET_PLAYER'][0] + pid, headers=self._headers)
        print(f'Get player {pid}')
        return res

    def get_map(self, map_name):
        res = request(self._links['GET_MAP'][1], self._links['GET_MAP'][0] + map_name, headers=self._headers)
        print(f'Get map {map_name}')
        return res

    def attack_cell(self, gid, pid, x, y):
        payload = {
            "Game": gid,
            "Player": pid,
            "X": x,
            "Y": y
        }
        res = request(self._links['ATTACK_CELL'][1], self._links['ATTACK_CELL'][0], json=payload, headers=self._headers)
        print(f'Attack cell <{x}, {y}>')
        return res
