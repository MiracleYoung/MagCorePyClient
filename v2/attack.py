#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/10 下午9:02
# @Author  : MiracleYoung
# @File    : attack.py


class Attack:
    def __init__(self, gid, pid, api):
        self._gid = gid
        self._pid = pid
        self._api = api

    def get_owner_cells(self, gid, idx):
        cells = self._api.get_game(gid).json()['Cells']
        return [[i, j] for i, row in enumerate(cells) for j, cell in enumerate(row) if cell['Owner'] == idx]

    def is_alive(self, pid):
        return self._api.get_player(pid).json()['State'] == 1

    def has_enemy(self, gid, idx):
        try:
            cells = self._api.get_game(gid).json()['Cells']
            for i, row in enumerate(cells):
                for j, cell in enumerate(row):
                    if cell['Owner'] not in (idx, 0):
                        return True
        except:
            pass
        finally:
            return False

    def attack_left(self, owner_cells, gid, pid):
        for x, y in owner_cells:
            if [x, y - 1] not in owner_cells and y - 1 >= 0:
                self._api.attack_cell(gid, pid, y - 1, x)

    def attack_right(self, owner_cells, gid, pid, max):
        for x, y in owner_cells:
            if [x, y + 1] not in owner_cells and y + 1 < max:
                self._api.attack_cell(gid, pid, y + 1, x)

    def attack_up(self, owner_cells, gid, pid, max):
        for x, y in owner_cells:
            if [x + 1, y] not in owner_cells and x + 1 < max:
                self._api.attack_cell(gid, pid, y, x + 1)

    def attack_down(self, owner_cells, gid, pid):
        for x, y in owner_cells:
            if [x - 1, y] not in owner_cells and x - 1 >= 0:
                self._api.attack_cell(gid, pid, y, x - 1)
